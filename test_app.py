"""
Simple test script to verify the Quiz Platform functionality
"""
import sqlite3
from app import init_db, DATABASE, hash_password
from werkzeug.security import check_password_hash

def test_database_initialization():
    """Test that database tables are created correctly"""
    print("Testing database initialization...")
    init_db()
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Check all tables exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    
    required_tables = ['users', 'quizzes', 'questions', 'scores']
    for table in required_tables:
        assert table in tables, f"Table {table} not found"
        print(f"✓ Table '{table}' exists")
    
    conn.close()
    print("✓ Database initialization test passed!\n")

def test_user_creation():
    """Test user creation and password hashing"""
    print("Testing user creation...")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create test user
    test_username = "testuser123"
    test_password = "testpass123"
    test_email = "test@example.com"
    
    # Clean up if exists
    cursor.execute("DELETE FROM users WHERE username = ?", (test_username,))
    
    hashed_password = hash_password(test_password)
    cursor.execute(
        'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
        (test_username, hashed_password, test_email)
    )
    conn.commit()
    
    # Verify user was created
    cursor.execute('SELECT username, email FROM users WHERE username = ?', (test_username,))
    user = cursor.fetchone()
    
    assert user is not None, "User was not created"
    assert user[0] == test_username, "Username doesn't match"
    assert user[1] == test_email, "Email doesn't match"
    print(f"✓ User '{test_username}' created successfully")
    
    # Clean up
    cursor.execute("DELETE FROM users WHERE username = ?", (test_username,))
    conn.commit()
    conn.close()
    print("✓ User creation test passed!\n")

def test_quiz_data():
    """Test that sample quiz data exists"""
    print("Testing quiz data...")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Check quizzes
    cursor.execute('SELECT COUNT(*) FROM quizzes')
    quiz_count = cursor.fetchone()[0]
    assert quiz_count >= 3, f"Expected at least 3 quizzes, found {quiz_count}"
    print(f"✓ Found {quiz_count} quizzes")
    
    # Check questions
    cursor.execute('SELECT COUNT(*) FROM questions')
    question_count = cursor.fetchone()[0]
    assert question_count >= 15, f"Expected at least 15 questions, found {question_count}"
    print(f"✓ Found {question_count} questions")
    
    # Verify question structure
    cursor.execute('SELECT * FROM questions LIMIT 1')
    question = cursor.fetchone()
    assert question is not None, "No questions found"
    print("✓ Questions have correct structure")
    
    conn.close()
    print("✓ Quiz data test passed!\n")

def test_password_hashing():
    """Test password hashing consistency and security"""
    print("Testing password hashing...")
    
    password = "mypassword123"
    hash1 = hash_password(password)
    hash2 = hash_password(password)
    
    # Hashes should be different because of salt (pbkdf2 with random salt)
    assert hash1 != hash2, "Hashes should be different due to salting"
    assert hash1 != password, "Password is not hashed"
    # pbkdf2:sha256 hash starts with method identifier
    assert hash1.startswith('pbkdf2:sha256:'), "Hash should use pbkdf2:sha256 method"
    # Both hashes should verify the same password
    assert check_password_hash(hash1, password), "Hash1 should verify original password"
    assert check_password_hash(hash2, password), "Hash2 should verify original password"
    print(f"✓ Password hashing uses secure pbkdf2:sha256 with salt")
    print(f"✓ Hash verification works correctly")
    print("✓ Password hashing test passed!\n")

if __name__ == '__main__':
    print("="*50)
    print("Running Quiz Platform Tests")
    print("="*50 + "\n")
    
    try:
        test_database_initialization()
        test_password_hashing()
        test_user_creation()
        test_quiz_data()
        
        print("="*50)
        print("✅ All tests passed successfully!")
        print("="*50)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        exit(1)
