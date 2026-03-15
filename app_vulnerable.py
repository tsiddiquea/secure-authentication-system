import sqlite3

# Create database and table if not exists
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

    # Insert default user if table empty
    cursor.execute("SELECT * FROM users")
    if not cursor.fetchall():
        cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
        conn.commit()

    conn.close()


def login():
    username = input("Username: ")
    password = input("Password: ")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # VULNERABLE QUERY
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("\nExecuting Query:", query)

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        print("Login Successful!")
    else:
        print("Login Failed.")

    conn.close()


if __name__ == "__main__":
    setup_database()
    login()