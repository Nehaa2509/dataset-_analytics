from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
from datetime import datetime
import hashlib
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for sessions

DATABASE = 'quiz_platform.db'

# Database helper functions
def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with tables"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Quizzes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Questions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_id INTEGER NOT NULL,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            points INTEGER DEFAULT 10,
            FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
        )
    ''')
    
    # User scores table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            quiz_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
        )
    ''')
    
    conn.commit()
    conn.close()

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    """Home page"""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        if not username or not password or not email:
            return render_template('register.html', error='All fields are required')
        
        conn = get_db()
        cursor = conn.cursor()
        
        try:
            hashed_password = hash_password(password)
            cursor.execute(
                'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                (username, hashed_password, email)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            conn.close()
            return render_template('register.html', error='Username or email already exists')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            return render_template('login.html', error='All fields are required')
        
        conn = get_db()
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        
        cursor.execute(
            'SELECT id, username FROM users WHERE username = ? AND password = ?',
            (username, hashed_password)
        )
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """User logout"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Get all available quizzes
    cursor.execute('SELECT * FROM quizzes ORDER BY created_at DESC')
    quizzes = cursor.fetchall()
    
    # Get user's recent scores
    cursor.execute('''
        SELECT s.score, s.total_questions, s.completed_at, q.title
        FROM scores s
        JOIN quizzes q ON s.quiz_id = q.id
        WHERE s.user_id = ?
        ORDER BY s.completed_at DESC
        LIMIT 5
    ''', (session['user_id'],))
    recent_scores = cursor.fetchall()
    
    conn.close()
    
    return render_template('dashboard.html', 
                         username=session['username'],
                         quizzes=quizzes,
                         recent_scores=recent_scores)

@app.route('/quiz/<int:quiz_id>')
@login_required
def take_quiz(quiz_id):
    """Take a quiz"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Get quiz details
    cursor.execute('SELECT * FROM quizzes WHERE id = ?', (quiz_id,))
    quiz = cursor.fetchone()
    
    if not quiz:
        conn.close()
        return redirect(url_for('dashboard'))
    
    # Get all questions for this quiz
    cursor.execute('SELECT * FROM questions WHERE quiz_id = ?', (quiz_id,))
    questions = cursor.fetchall()
    
    conn.close()
    
    return render_template('quiz.html', quiz=quiz, questions=questions)

@app.route('/submit_quiz/<int:quiz_id>', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    """Submit quiz answers and calculate score"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Get all questions for this quiz
    cursor.execute('SELECT id, correct_answer, points FROM questions WHERE quiz_id = ?', (quiz_id,))
    questions = cursor.fetchall()
    
    score = 0
    total_points = 0
    
    # Calculate score
    for question in questions:
        total_points += question['points']
        user_answer = request.form.get(f'question_{question["id"]}')
        if user_answer and user_answer.upper() == question['correct_answer'].upper():
            score += question['points']
    
    # Save score to database
    cursor.execute(
        'INSERT INTO scores (user_id, quiz_id, score, total_questions) VALUES (?, ?, ?, ?)',
        (session['user_id'], quiz_id, score, len(questions))
    )
    conn.commit()
    conn.close()
    
    return redirect(url_for('result', quiz_id=quiz_id, score=score, total=total_points))

@app.route('/result')
@login_required
def result():
    """Show quiz result"""
    quiz_id = request.args.get('quiz_id')
    score = request.args.get('score')
    total = request.args.get('total')
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT title FROM quizzes WHERE id = ?', (quiz_id,))
    quiz = cursor.fetchone()
    conn.close()
    
    return render_template('result.html', 
                         quiz_title=quiz['title'] if quiz else 'Quiz',
                         score=score, 
                         total=total)

@app.route('/leaderboard')
@login_required
def leaderboard():
    """Show leaderboard"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Get top scores across all quizzes
    cursor.execute('''
        SELECT u.username, q.title as quiz_title, s.score, s.total_questions, s.completed_at
        FROM scores s
        JOIN users u ON s.user_id = u.id
        JOIN quizzes q ON s.quiz_id = q.id
        ORDER BY s.score DESC, s.completed_at ASC
        LIMIT 20
    ''')
    top_scores = cursor.fetchall()
    
    conn.close()
    
    return render_template('leaderboard.html', scores=top_scores)

# API endpoints for dynamic interaction
@app.route('/api/quizzes')
@login_required
def api_get_quizzes():
    """Get all quizzes (API endpoint)"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM quizzes')
    quizzes = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(quiz) for quiz in quizzes])

@app.route('/api/quiz/<int:quiz_id>/questions')
@login_required
def api_get_questions(quiz_id):
    """Get questions for a quiz (API endpoint)"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, question_text, option_a, option_b, option_c, option_d FROM questions WHERE quiz_id = ?', (quiz_id,))
    questions = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(q) for q in questions])

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
