import sqlite3
from app import init_db, DATABASE

def populate_sample_data():
    """Populate database with sample quiz data"""
    
    # Initialize database first
    init_db()
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Check if data already exists
    cursor.execute('SELECT COUNT(*) FROM quizzes')
    if cursor.fetchone()[0] > 0:
        print("Sample data already exists!")
        conn.close()
        return
    
    # Add sample quizzes
    quizzes = [
        ("Python Basics", "Test your knowledge of Python fundamentals"),
        ("Web Development", "HTML, CSS, and JavaScript basics"),
        ("Data Structures", "Common data structures and algorithms"),
    ]
    
    for title, description in quizzes:
        cursor.execute(
            'INSERT INTO quizzes (title, description) VALUES (?, ?)',
            (title, description)
        )
    
    # Add sample questions for Python Basics (quiz_id = 1)
    python_questions = [
        ("What is the correct file extension for Python files?", ".py", ".python", ".pt", ".pyt", "A"),
        ("Which keyword is used to define a function in Python?", "function", "def", "fun", "define", "B"),
        ("What is the output of: print(2 ** 3)?", "6", "8", "9", "5", "B"),
        ("Which of the following is a mutable data type in Python?", "tuple", "string", "list", "int", "C"),
        ("How do you create a comment in Python?", "// comment", "/* comment */", "# comment", "-- comment", "C"),
    ]
    
    for q_text, opt_a, opt_b, opt_c, opt_d, correct in python_questions:
        cursor.execute(
            '''INSERT INTO questions (quiz_id, question_text, option_a, option_b, option_c, option_d, correct_answer, points)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (1, q_text, opt_a, opt_b, opt_c, opt_d, correct, 10)
        )
    
    # Add sample questions for Web Development (quiz_id = 2)
    web_questions = [
        ("What does HTML stand for?", "Hyper Text Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language", "A"),
        ("Which HTML tag is used for the largest heading?", "<heading>", "<h6>", "<h1>", "<head>", "C"),
        ("Which CSS property is used to change the text color?", "text-color", "font-color", "color", "text-style", "C"),
        ("What does CSS stand for?", "Cascading Style Sheets", "Computer Style Sheets", "Creative Style Sheets", "Colorful Style Sheets", "A"),
        ("Which JavaScript method is used to write into an HTML element?", "innerHTML", "writeHTML", "documentWrite", "elementWrite", "A"),
    ]
    
    for q_text, opt_a, opt_b, opt_c, opt_d, correct in web_questions:
        cursor.execute(
            '''INSERT INTO questions (quiz_id, question_text, option_a, option_b, option_c, option_d, correct_answer, points)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (2, q_text, opt_a, opt_b, opt_c, opt_d, correct, 10)
        )
    
    # Add sample questions for Data Structures (quiz_id = 3)
    ds_questions = [
        ("Which data structure uses LIFO (Last In First Out)?", "Queue", "Stack", "Array", "Tree", "B"),
        ("Which data structure uses FIFO (First In First Out)?", "Stack", "Tree", "Queue", "Graph", "C"),
        ("What is the time complexity of accessing an element in an array by index?", "O(n)", "O(log n)", "O(1)", "O(n^2)", "C"),
        ("Which data structure is best for implementing a priority queue?", "Array", "Linked List", "Heap", "Stack", "C"),
        ("In a binary tree, what is the maximum number of children a node can have?", "1", "2", "3", "Unlimited", "B"),
    ]
    
    for q_text, opt_a, opt_b, opt_c, opt_d, correct in ds_questions:
        cursor.execute(
            '''INSERT INTO questions (quiz_id, question_text, option_a, option_b, option_c, option_d, correct_answer, points)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (3, q_text, opt_a, opt_b, opt_c, opt_d, correct, 10)
        )
    
    conn.commit()
    conn.close()
    
    print("Sample data populated successfully!")
    print("\nQuizzes added:")
    print("1. Python Basics - 5 questions")
    print("2. Web Development - 5 questions")
    print("3. Data Structures - 5 questions")

if __name__ == '__main__':
    populate_sample_data()
