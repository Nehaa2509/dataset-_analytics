# How to Use on Replit - Quick Start Guide

This guide shows you how to deploy and use the Online Quiz Platform on Replit.

## Step 1: Import to Replit

1. Go to [Replit.com](https://replit.com) and sign in
2. Click the "+" button or "Create Repl"
3. Select "Import from GitHub"
4. Paste your repository URL
5. Click "Import from GitHub"

## Step 2: Setup (First Time Only)

Once the Repl is created, you need to set up the database:

1. In the Shell tab, run:
   ```bash
   python populate_data.py
   ```
   This creates the database and adds 3 sample quizzes with 15 questions.

2. (Optional) Set environment variables for production:
   - Click on "Secrets" (🔒 icon) in the left sidebar
   - Add a secret named `SECRET_KEY` with a random value (e.g., generated from a password generator)
   - This ensures user sessions persist across restarts

## Step 3: Run the Application

1. Click the green "Run" button at the top
2. The application will start and open in the webview
3. The URL will be something like: `https://your-repl-name.username.repl.co`

## Step 4: Use the Platform

### For Users:

1. **Register an Account**
   - Click "Register" or "Get Started"
   - Enter username (3-50 characters)
   - Enter email address
   - Enter password (minimum 6 characters)
   - Click "Register"

2. **Login**
   - Enter your username and password
   - Click "Login"

3. **Take a Quiz**
   - From the dashboard, you'll see available quizzes
   - Click "Start Quiz" on any quiz
   - Answer all questions by selecting A, B, C, or D
   - Click "Submit Quiz" when done

4. **View Results**
   - Your score will be shown immediately
   - You'll see your percentage and performance message
   - Click "Back to Dashboard" to take more quizzes

5. **Check the Leaderboard**
   - Click "Leaderboard" in the navigation
   - See top scores from all users
   - Top 3 positions get medal icons (🥇🥈🥉)

### Default Sample Quizzes:

1. **Python Basics** - 5 questions on Python fundamentals
2. **Web Development** - 5 questions on HTML, CSS, JavaScript
3. **Data Structures** - 5 questions on common data structures

Each question is worth 10 points.

## Step 5: Customization (Optional)

### Adding More Quizzes

You can add more quizzes by modifying `populate_data.py`:

```python
# Add this before the conn.commit() line in populate_data.py
cursor.execute(
    'INSERT INTO quizzes (title, description) VALUES (?, ?)',
    ('Your Quiz Title', 'Description of your quiz')
)
quiz_id = cursor.lastrowid  # Get the ID of the quiz you just added

# Add questions for your quiz
questions = [
    ("Question text?", "Option A", "Option B", "Option C", "Option D", "A"),
    # Add more questions...
]

for q_text, opt_a, opt_b, opt_c, opt_d, correct in questions:
    cursor.execute(
        '''INSERT INTO questions (quiz_id, question_text, option_a, option_b, option_c, option_d, correct_answer, points)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (quiz_id, q_text, opt_a, opt_b, opt_c, opt_d, correct, 10)
    )
```

Then re-run:
```bash
rm quiz_platform.db
python populate_data.py
```

### Changing Colors/Styling

All styles are in `templates/base.html`. Look for the `<style>` section and modify colors:
- Primary color: `#667eea` (purple)
- Secondary gradient: `#764ba2` (darker purple)
- Success: `#28a745` (green)
- Warning: `#ffc107` (yellow)
- Error: `#dc3545` (red)

## Troubleshooting

**Problem: "Database file not found" error**
- Solution: Run `python populate_data.py` in the Shell

**Problem: Users get logged out when Repl restarts**
- Solution: Set a `SECRET_KEY` environment variable in Secrets (🔒)

**Problem: Can't access the website**
- Solution: Click the "Run" button again, or click "Open in new tab" (↗️) 

**Problem: Application runs but shows errors**
- Solution: Check the Console tab for error messages

## Production Deployment Tips

For serious production use on Replit:

1. **Set Environment Variables:**
   ```
   SECRET_KEY=your-long-random-secret-key-here
   DEBUG=false
   ```

2. **Enable Always On** (if you have Replit's Hacker plan):
   - This keeps your Repl running 24/7
   - Otherwise, the Repl will sleep after inactivity

3. **Backup Your Database:**
   - Download `quiz_platform.db` regularly
   - Or implement automated backups

4. **Monitor Usage:**
   - Watch for unusual activity
   - Check the leaderboard for suspicious scores

## Advanced Features You Can Add

- **Timer for quizzes**: Add JavaScript countdown timer
- **Question categories**: Add category field to questions table
- **Difficulty levels**: Add difficulty rating (easy/medium/hard)
- **Quiz attempts limit**: Track how many times a user took each quiz
- **Question shuffling**: Randomize question and answer order
- **Admin panel**: Create interface to add quizzes without editing code
- **Email verification**: Send confirmation emails on registration
- **Password reset**: Implement forgot password functionality
- **Profile pictures**: Allow users to upload avatars
- **Achievements/Badges**: Award badges for milestones

## Getting Help

If you encounter issues:
1. Check the Console tab for Python errors
2. Check the browser's Developer Tools console for JavaScript errors
3. Review the code in `app.py` to understand the flow
4. Check `QUIZ_README.md` for detailed documentation

Enjoy your quiz platform! 🎯
