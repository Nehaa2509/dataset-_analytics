from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS progress 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  date TEXT, 
                  habit_name TEXT, 
                  status INTEGER,
                  UNIQUE(date, habit_name))''')
    conn.commit()
    conn.close()

HABITS = [
    "Wake Up (5AM)", "Study", "Workout", "Meditation", 
    "Cold Shower", "Water Intake", "Journal", "No Scrolling"
]

def get_week_dates():
    """Get the current week dates (Monday to Sunday)"""
    today = datetime.now()
    # Find the Monday of the current week
    start_of_week = today - timedelta(days=today.weekday())
    dates = []
    for i in range(7):
        date = start_of_week + timedelta(days=i)
        dates.append(date.strftime('%Y-%m-%d'))
    return dates

@app.route('/')
def index():
    week_dates = get_week_dates()
    today = datetime.now()
    week_number = today.isocalendar()[1]
    return render_template('index.html', 
                         habits=HABITS, 
                         dates=week_dates,
                         week_number=week_number,
                         today=datetime.now().strftime('%Y-%m-%d'))

@app.route('/update', methods=['POST'])
def update_habit():
    data = request.json
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    # Logic to upsert (update or insert) the habit status
    # First try to update existing record
    c.execute("UPDATE progress SET status = ? WHERE date = ? AND habit_name = ?",
              (data['status'], data['date'], data['habit_name']))
    # If no rows were updated, insert a new record
    if c.rowcount == 0:
        c.execute("INSERT INTO progress (date, habit_name, status) VALUES (?, ?, ?)",
                  (data['date'], data['habit_name'], data['status']))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

@app.route('/get_data', methods=['GET'])
def get_data():
    """Get all habit data for the current week"""
    week_dates = get_week_dates()
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    
    # Fetch all data for the week
    c.execute("""SELECT date, habit_name, status FROM progress 
                 WHERE date IN ({})""".format(','.join('?' * len(week_dates))), week_dates)
    rows = c.fetchall()
    conn.close()
    
    # Convert to a dictionary for easy access
    data = {}
    for row in rows:
        key = f"{row[0]}_{row[1]}"
        data[key] = row[2]
    
    return jsonify(data)

@app.route('/get_progress', methods=['GET'])
def get_progress():
    """Get daily progress scores for the chart"""
    week_dates = get_week_dates()
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    
    progress_data = []
    for date in week_dates:
        c.execute("SELECT COUNT(*) FROM progress WHERE date = ? AND status = 1", (date,))
        completed = c.fetchone()[0]
        progress_data.append(completed)
    
    conn.close()
    return jsonify(progress_data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
