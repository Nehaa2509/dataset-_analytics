# 🚀 Deployment Checklist for Replit

Use this checklist when deploying the Online Quiz Platform to Replit.

## Pre-Deployment

- [ ] Repository is pushed to GitHub
- [ ] All files are committed
- [ ] .gitignore is configured to exclude quiz_platform.db

## Replit Setup

- [ ] Created new Repl
- [ ] Imported from GitHub repository
- [ ] Repl loaded successfully

## Initial Configuration

- [ ] Run `python populate_data.py` in Shell
- [ ] Verify output shows "3 Quizzes added"
- [ ] Check that `quiz_platform.db` file was created

## Environment Variables (Optional but Recommended)

- [ ] Click on Secrets (🔒) icon
- [ ] Add `SECRET_KEY` with a random string
- [ ] (Optional) Add `DEBUG=false` for production

## First Run

- [ ] Click green "Run" button
- [ ] Wait for Flask server to start
- [ ] Look for "Running on http://0.0.0.0:5000" message
- [ ] Webview should open automatically

## Testing Basic Functionality

### Test Registration
- [ ] Click "Register" or "Get Started"
- [ ] Create account (username, email, password)
- [ ] Successfully redirected to login page

### Test Login
- [ ] Enter credentials
- [ ] Successfully logged in
- [ ] Dashboard displays with 3 quizzes

### Test Quiz Taking
- [ ] Click "Start Quiz" on any quiz
- [ ] All questions display correctly
- [ ] Answer all questions
- [ ] Click "Submit Quiz"
- [ ] Results page shows score

### Test Leaderboard
- [ ] Click "Leaderboard" in navigation
- [ ] Your score appears in the list
- [ ] Top 3 positions show medal icons

### Test Logout
- [ ] Click "Logout"
- [ ] Redirected to home page
- [ ] Cannot access dashboard without logging in

## Production Settings (For Public Deployment)

- [ ] Set `SECRET_KEY` environment variable
- [ ] Ensure `DEBUG` is not set or set to `false`
- [ ] Test from different browser/incognito mode
- [ ] Share Repl URL with others to test

## Troubleshooting

If something doesn't work:

1. **Check Shell/Console for errors**
   - Look for Python tracebacks
   - Common issue: Database not initialized
   - Solution: Run `python populate_data.py`

2. **If "Database is locked" error**
   - Stop the application
   - Delete `quiz_platform.db`
   - Run `python populate_data.py` again
   - Restart application

3. **If users get logged out on restart**
   - Set `SECRET_KEY` environment variable
   - This makes sessions persist

4. **If pages don't load**
   - Check that Flask server started
   - Look for "Running on" message in console
   - Try stopping and starting again

5. **If styles don't appear**
   - Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
   - Check that templates/base.html exists

## Verification Commands

Run these in the Shell to verify everything:

```bash
# Check files exist
ls -la

# Count templates
ls templates/ | wc -l
# Should output: 8

# Check database
python -c "import sqlite3; c = sqlite3.connect('quiz_platform.db'); print('Quizzes:', c.execute('SELECT COUNT(*) FROM quizzes').fetchone()[0])"
# Should output: Quizzes: 3

# Run tests
python test_app.py
# Should output: ✅ All tests passed successfully!
```

## Success Criteria

✅ All of the following should be true:
- Application starts without errors
- Can register new users
- Can login with credentials
- Can take quizzes and get scores
- Scores appear on leaderboard
- Can logout successfully
- No security vulnerabilities (CodeQL scan passed)

## Post-Deployment

- [ ] Share Repl URL with users
- [ ] Monitor usage in Console
- [ ] Backup database regularly (download quiz_platform.db)
- [ ] Update quizzes as needed using populate_data.py

## Quick Reference

**Main Files:**
- `app.py` - Flask application
- `populate_data.py` - Database setup
- `test_app.py` - Test suite
- `templates/` - HTML pages
- `quiz_platform.db` - SQLite database

**Key URLs:**
- `/` - Home page
- `/register` - Registration
- `/login` - Login
- `/dashboard` - User dashboard
- `/quiz/<id>` - Take quiz
- `/leaderboard` - View rankings

**Environment Variables:**
- `SECRET_KEY` - For session persistence (recommended)
- `DEBUG` - Set to "true" for development only

---

**Status**: Ready for deployment ✅

Use REPLIT_GUIDE.md for detailed step-by-step instructions.
