import sqlite3
import hashlib
import datetime

DB_PATH = "users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Create users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            created_at TEXT
        )
    ''')
    
    # Optional: activity log for cybersecurity tracking
    c.execute('''
        CREATE TABLE IF NOT EXISTS activity_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action TEXT,
            timestamp TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize DB at import
init_db()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)",
                  (username, hash_password(password), str(datetime.datetime.now())))
        conn.commit()
        conn.close()
        return True, "User registered successfully."
    except sqlite3.IntegrityError:
        return False, "Username already exists."
    except Exception as e:
        return False, str(e)

def login_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, password FROM users WHERE username=?", (username,))
    row = c.fetchone()
    conn.close()
    if row and hash_password(password) == row[1]:
        return True, row[0], "user"
    else:
        return False, None, None
def log_activity(user_id, action, extra=None):
    import sqlite3, datetime
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    ts = str(datetime.datetime.now())
    
    if extra is not None:
        action = f"{action}: {extra}"
    
    c.execute("INSERT INTO activity_log (user_id, action, timestamp) VALUES (?, ?, ?)",
              (user_id, action, ts))
    conn.commit()
    conn.close()
