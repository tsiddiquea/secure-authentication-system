import sqlite3
import datetime

def setup_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    cursor.execute("SELECT * FROM users")
    if not cursor.fetchall():
        cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
        conn.commit()

    conn.close()


def log_attack(input_data):
    with open("attack_logs.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} - Suspicious input detected: {input_data}\n")


def detect_injection(user_input):
    suspicious_patterns = ["'", "--", ";", " OR ", " AND "]
    for pattern in suspicious_patterns:
        if pattern.lower() in user_input.lower():
            return True
    return False


def login():
    username = input("Username: ")
    password = input("Password: ")

    # Detect suspicious input
    if detect_injection(username) or detect_injection(password):
        print("⚠ Warning: Possible SQL Injection attempt detected!")
        log_attack(username + " | " + password)

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    #  SECURE PARAMETERIZED QUERY
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    result = cursor.fetchone()

    if result:
        print("Login Successful!")
    else:
        print("Login Failed.")

    conn.close()


if __name__ == "__main__":
    setup_database()
    login()