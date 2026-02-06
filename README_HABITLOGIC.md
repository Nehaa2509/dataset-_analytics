# HabitLogic - Habit Tracker Web Application

A Flask-based web application for tracking daily habits with visual progress analytics.

## 📋 Features

- **Dynamic 7-Day Grid**: Track up to 8 different habits across a weekly view
- **Binary Check System**: Simple toggle checkboxes for habit completion (✓ or ✗)
- **Live Analytics**: Real-time statistics showing:
  - Total number of habits
  - Habits completed today
  - Daily completion percentage
- **Weekly Progress Chart**: Visual line chart showing habits completed per day
- **Data Persistence**: SQLite database ensures your data is saved between sessions
- **Responsive Design**: Clean, notebook-style interface with custom styling

## 🎯 Default Habits

1. Wake Up (5AM)
2. Study
3. Workout
4. Meditation
5. Cold Shower
6. Water Intake
7. Journal
8. No Scrolling

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Nehaa2509/dataset-_analytics.git
cd dataset-_analytics
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Start tracking your habits!

## 💾 Database

The application uses SQLite for data storage. The database file `habits.db` is automatically created when you first run the application.

### Database Schema

```sql
CREATE TABLE progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    habit_name TEXT,
    status INTEGER,
    UNIQUE(date, habit_name)
)
```

## 🎨 Customization

### Modifying Habits

To change the list of habits, edit the `HABITS` list in `app.py`:

```python
HABITS = [
    "Your Custom Habit 1",
    "Your Custom Habit 2",
    # Add more habits here
]
```

### Styling

The application uses embedded CSS in `templates/index.html`. You can modify colors, fonts, and layout by editing the `<style>` section.

## 📊 Progress Chart

The application includes two chart rendering modes:

1. **Chart.js Mode**: If Chart.js loads successfully, displays an interactive chart
2. **Fallback Mode**: Custom canvas-based chart when Chart.js is unavailable

Both modes provide the same visual representation of your weekly progress.

## 🛠️ Technical Architecture

### Backend (`app.py`)
- Flask web framework
- SQLite database operations
- RESTful API endpoints:
  - `GET /` - Main page
  - `POST /update` - Update habit status
  - `GET /get_data` - Fetch all habit data
  - `GET /get_progress` - Get progress statistics

### Frontend (`templates/index.html`)
- Responsive HTML table for habit grid
- JavaScript for dynamic updates
- Canvas-based chart visualization
- Fetch API for backend communication

## 📁 Project Structure

```
dataset-_analytics/
├── app.py                      # Flask backend
├── templates/
│   └── index.html             # Frontend template
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
├── README.md                 # This file
└── habits.db                 # SQLite database (auto-generated)
```

## 🔧 API Endpoints

### Update Habit Status
```
POST /update
Content-Type: application/json

{
    "date": "2026-02-06",
    "habit_name": "Study",
    "status": 1
}
```

### Get All Data
```
GET /get_data

Returns: JSON object with habit statuses
```

### Get Progress Data
```
GET /get_progress

Returns: Array of daily completion counts
```

## 📝 Development

### Running in Debug Mode

The application runs in debug mode by default:

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

For production, change `debug=True` to `debug=False`.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## 📄 License

This project is open source and available for educational purposes.

## 🎓 Learning Resources

This project demonstrates:
- Flask web framework basics
- SQLite database integration
- RESTful API design
- JavaScript DOM manipulation
- Canvas API for custom graphics
- Responsive web design

## 🙏 Acknowledgments

Built as part of a Software Project Management (SPM) exercise to transform an idea into a working application using systematic development practices.
