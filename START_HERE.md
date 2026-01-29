# 🎯 Online Quiz Platform - START HERE

Welcome! This repository contains a complete **Online Quiz Platform** backend built with Flask and SQLite, ready to deploy on Replit.

## ⚡ Quick Start (3 Steps)

### On Replit (Easiest)
1. **Import**: Import this repo to Replit
2. **Setup**: Run `python populate_data.py` in Shell
3. **Launch**: Click the "Run" button

👉 **Detailed guide**: See [REPLIT_GUIDE.md](REPLIT_GUIDE.md)

### Locally
1. **Install**: `pip install -r requirements.txt`
2. **Setup**: `python populate_data.py`
3. **Run**: `python app.py`

## 📚 Documentation

Choose the guide that fits your needs:

| Document | Purpose | When to Use |
|----------|---------|-------------|
| **[REPLIT_GUIDE.md](REPLIT_GUIDE.md)** | Step-by-step Replit deployment | Deploying to Replit for the first time |
| **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** | Deployment verification checklist | During and after deployment |
| **[QUIZ_README.md](QUIZ_README.md)** | Technical documentation & API | Understanding code structure, adding features |
| **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** | Complete project overview | Understanding what was built and why |
| **This file (START_HERE.md)** | Quick navigation guide | Finding the right documentation |

## 🎮 What You Get

### For Users
- ✅ Register and login securely
- ✅ Take quizzes on Python, Web Dev, and Data Structures
- ✅ Get instant scores and feedback
- ✅ Compete on the leaderboard

### For Developers
- ✅ Clean Flask application structure
- ✅ SQLite database with 4 tables
- ✅ 8 responsive HTML templates
- ✅ Secure authentication (pbkdf2:sha256)
- ✅ Comprehensive test suite
- ✅ Production-ready security

## 🔐 Security Features

- ✅ **Secure password hashing** with salt (pbkdf2:sha256)
- ✅ **SQL injection prevention** via parameterized queries
- ✅ **Score validation** on server-side
- ✅ **Input validation** for all user inputs
- ✅ **Debug mode** disabled in production
- ✅ **CodeQL scan**: 0 vulnerabilities

## 📊 Sample Data Included

- **3 Quizzes**: Python Basics, Web Development, Data Structures
- **15 Questions**: 5 per quiz, multiple choice (A/B/C/D)
- **Points**: 10 points per correct answer

## 🛠️ Tech Stack

- **Backend**: Flask 2.3.3
- **Database**: SQLite
- **Frontend**: HTML + CSS (embedded)
- **Auth**: Session-based with Werkzeug password hashing
- **Deployment**: Replit-ready

## 📁 Key Files

```
├── app.py                      # Main Flask application (10KB)
├── populate_data.py            # Database setup script
├── test_app.py                 # Test suite (all tests passing ✅)
├── requirements.txt            # Python dependencies
├── .replit                     # Replit configuration
├── templates/                  # 8 HTML templates
│   ├── base.html              # Base template with styling
│   ├── index.html             # Home page
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   ├── dashboard.html         # User dashboard
│   ├── quiz.html              # Quiz taking page
│   ├── result.html            # Results page
│   └── leaderboard.html       # Leaderboard
└── docs/                       # 5 documentation files
    ├── REPLIT_GUIDE.md
    ├── DEPLOYMENT_CHECKLIST.md
    ├── QUIZ_README.md
    ├── PROJECT_SUMMARY.md
    └── START_HERE.md (you are here)
```

## 🚀 First-Time Setup

### Step 1: Initialize Database
```bash
python populate_data.py
```

Expected output:
```
Sample data populated successfully!

Quizzes added:
1. Python Basics - 5 questions
2. Web Development - 5 questions
3. Data Structures - 5 questions
```

### Step 2: Run Application
```bash
python app.py
```

Expected output:
```
* Serving Flask app 'app'
* Debug mode: off
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
```

### Step 3: Test Everything
```bash
python test_app.py
```

Expected output:
```
==================================================
✅ All tests passed successfully!
==================================================
```

## 🎯 Common Tasks

### Add a New Quiz
Edit `populate_data.py` and add your quiz data, then:
```bash
rm quiz_platform.db
python populate_data.py
```

### Change Styling
Edit `templates/base.html` (look for `<style>` section)

### View Database
```bash
sqlite3 quiz_platform.db
.tables
SELECT * FROM quizzes;
```

### Enable Debug Mode (Development Only)
```bash
DEBUG=true python app.py
```

### Set Production Secret Key
```bash
SECRET_KEY=your-random-secret-key python app.py
```

## 🐛 Troubleshooting

**Problem**: Database not found
```bash
# Solution:
python populate_data.py
```

**Problem**: Users logged out after restart
```bash
# Solution: Set SECRET_KEY environment variable
export SECRET_KEY=your-secret-key
python app.py
```

**Problem**: Want to reset everything
```bash
# Solution:
rm quiz_platform.db
python populate_data.py
```

## 📖 Learning Resources

- **Flask Tutorial**: https://flask.palletsprojects.com/
- **SQLite Documentation**: https://www.sqlite.org/docs.html
- **Jinja2 Templates**: https://jinja.palletsprojects.com/

## 🆘 Need Help?

1. Check [REPLIT_GUIDE.md](REPLIT_GUIDE.md) for deployment issues
2. Check [QUIZ_README.md](QUIZ_README.md) for technical questions
3. Check [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) for verification steps
4. Run `python test_app.py` to verify installation

## ⭐ Features to Add (Ideas)

- Timer for quizzes
- Admin panel for quiz management
- Question categories and difficulty levels
- Email verification
- Profile pictures
- Achievements/badges
- Export results to PDF

See [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for more enhancement ideas.

## ✅ Ready to Deploy?

Follow this order:
1. Read this file (you're here! ✅)
2. Follow [REPLIT_GUIDE.md](REPLIT_GUIDE.md) for deployment
3. Use [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) to verify
4. Refer to [QUIZ_README.md](QUIZ_README.md) for customization

---

**Status**: Production Ready ✅ | **Security**: 0 Vulnerabilities ✅ | **Tests**: All Passing ✅

**Happy Quizzing! 🎯**
