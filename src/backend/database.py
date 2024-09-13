import sqlite3
import bcrypt

class Database:
    def __init__(self, db_file = "safeKeeper.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()


    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT UNIQUE NOT NULL,
           password TEXT NOT NULL                                  
                            )
        ''')
        #Add a table for storing passwords
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()

class User:
    def __init__(self, db):
        self.db = db

    def register(self, username, password):
        #hash the password using bcrypt
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            self.db.cursor.execute("INSERT INTO users (username, password) VALUES(?, ?)", (username, hashed))
            self.db.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        

    def login(self, username, password):
        # Fetch the hashed password from the database
        self.db.cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = self.db.cursor.fetchone()

        # Debug: Print retrieved password
        print(f"Stored password hash for {username}: {result}")

        if result:
            stored_hashed_password = result[0]

            # Convert stored password to bytes if it's a string
            if isinstance(stored_hashed_password, str):
                stored_hashed_password = stored_hashed_password.encode('utf-8')

            # Debug: Print password comparison result
            print(f"Comparing {password} with stored hash")

            # Compare the provided password with the stored hash
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                print("Password match!")
                return True
            else:
                print("Password does not match.")
                return False

        return False
    def get_user_id(self, username):
        self.db.cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        result = self.db.cursor.fetchone()
        return result[0] if result else None
    
    def add_passwword(self,user_id, website, username, password):
        self.db.cursor.execute("INSERT INTO passwords (user_id, website, username, password) VALUES (?,?,?,?)",
                               (user_id, website, username, password))
        self.db.conn.commit()

    def get_passwords(self, user_id):
        self.db.cursor.execute("SELECT website, username, password FROM passwords WHERE user_id= ?", (user_id,))
        return self.db.cursor.fetchall()

        