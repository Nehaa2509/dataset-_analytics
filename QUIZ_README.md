# Online Quiz Platform 🎯

A simple yet powerful online quiz platform built with Flask and SQLite. Perfect for running on Replit!

## Features

- ✅ User Registration & Login
- 📝 Multiple Quiz Support
- ⏱️ Real-time Scoring
- 🏆 Leaderboard System
- 📊 User Dashboard
- 🎨 Modern, Responsive UI

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS (embedded in templates)
- **Authentication**: Session-based with password hashing

## Quick Start on Replit

1. **Import this repository to Replit**
   - Go to [Replit](https://replit.com)
   - Click "Create Repl"
   - Choose "Import from GitHub"
   - Paste the repository URL

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Populate sample data**
   ```bash
   python populate_data.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   Or simply click the "Run" button in Replit!
   
   **Optional**: Enable debug mode for development:
   ```bash
   DEBUG=true python app.py
   ```

5. **Access the application**
   - The app will run on `http://0.0.0.0:5000`
   - In Replit, it will automatically open in the webview

## Quick Start Locally

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd dataset-_analytics
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Populate sample data**
   ```bash
   python populate_data.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   
   **Optional**: Enable debug mode for development:
   ```bash
   DEBUG=true python app.py
   ```
   
   **Optional**: Set a custom secret key for production:
   ```bash
   SECRET_KEY=your-secret-key-here python app.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:5000`

## Usage

### For Users

1. **Register**: Create a new account with username, email, and password
2. **Login**: Access your account
3. **Take Quizzes**: Choose from available quizzes and answer questions
4. **View Results**: Get immediate feedback on your performance
5. **Check Leaderboard**: See how you rank against other users

### For Developers

#### Database Schema

**Users Table**
- `id`: Primary key
- `username`: Unique username
- `password`: Hashed password
- `email`: Unique email
- `created_at`: Registration timestamp

**Quizzes Table**
- `id`: Primary key
- `title`: Quiz title
- `description`: Quiz description
- `created_at`: Creation timestamp

**Questions Table**
- `id`: Primary key
- `quiz_id`: Foreign key to quizzes
- `question_text`: The question
- `option_a`, `option_b`, `option_c`, `option_d`: Answer options
- `correct_answer`: Correct answer (A, B, C, or D)
- `points`: Points for correct answer

**Scores Table**
- `id`: Primary key
- `user_id`: Foreign key to users
- `quiz_id`: Foreign key to quizzes
- `score`: Points earned
- `total_questions`: Total questions in quiz
- `completed_at`: Completion timestamp

#### Adding New Quizzes

You can add new quizzes by modifying `populate_data.py` or by directly inserting into the database:

```python
# Add a new quiz
cursor.execute(
    'INSERT INTO quizzes (title, description) VALUES (?, ?)',
    ('Your Quiz Title', 'Quiz Description')
)

# Add questions for the quiz
cursor.execute(
    '''INSERT INTO questions (quiz_id, question_text, option_a, option_b, option_c, option_d, correct_answer, points)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
    (quiz_id, 'Question text?', 'Option A', 'Option B', 'Option C', 'Option D', 'A', 10)
)
```

## API Endpoints

### Authentication
- `GET /`: Home page
- `GET/POST /register`: User registration
- `GET/POST /login`: User login
- `GET /logout`: User logout

### Quiz Management
- `GET /dashboard`: User dashboard with available quizzes
- `GET /quiz/<quiz_id>`: Take a specific quiz
- `POST /submit_quiz/<quiz_id>`: Submit quiz answers
- `GET /result`: View quiz results

### Leaderboard
- `GET /leaderboard`: View global leaderboard

### API Endpoints (JSON)
- `GET /api/quizzes`: Get all quizzes (JSON)
- `GET /api/quiz/<quiz_id>/questions`: Get questions for a quiz (JSON)

## Sample Quizzes Included

1. **Python Basics** - 5 questions on Python fundamentals
2. **Web Development** - 5 questions on HTML, CSS, and JavaScript
3. **Data Structures** - 5 questions on common data structures

## Security Features

- Secure password hashing using Werkzeug's pbkdf2:sha256 with salt
- Session-based authentication with persistent secret key
- Login required decorators for protected routes
- SQL injection prevention using parameterized queries
- Password minimum length validation (6 characters)
- Username length validation (3-50 characters)
- Debug mode disabled by default (enable via DEBUG environment variable)

## Customization

### Styling
- All CSS is embedded in `templates/base.html`
- Modify the `<style>` section to change colors, fonts, etc.

### Adding Features
- Timer for quizzes: Add JavaScript timer in quiz.html
- Question categories: Add a category field to questions table
- Difficulty levels: Add difficulty field to questions
- Multiple attempts: Track attempt numbers in scores table

## Troubleshooting

**Database not found?**
- Run `python populate_data.py` to initialize the database

**Port already in use?**
- Change the port in `app.py`: `app.run(host='0.0.0.0', port=8080)`

**Dependencies not installing?**
- Ensure you have Python 3.7+ installed
- Try `pip install --upgrade pip` first

## Contributing

Feel free to fork this repository and add your own features!

## License

This project is open source and available for educational purposes.

## Author

Created as a simple, Replit-ready quiz platform for learning Flask and web development.
