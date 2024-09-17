import sqlite3
import bcrypt
from cryptography.fernet import Fernet
import os

class Database:
    def __init__(self, db_file = "safeKeeper.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.key = self.load_or_generate_key() # to handle key management.
        self.cipher_suite = Fernet(self.key)
    


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

    def load_or_generate_key(self):
        key_file = "encryption.key"
        if os.path.exists(key_file):
            with open(key_file, "rb") as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, "wb") as file:
                file.write(key)
            return key
        
    def encrypt_password(self, password):
        return self.cipher_suite.encrypt(password.encode()).decode()
    
    def decrypt_password(self, encrypt_password):
        return self.cipher_suite.decrypt(encrypt_password.encode()).decode()

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
    
    def add_password(self,user_id, website, username, password):
        encrypted_passwords = self.db.encrypt_password(password)
        self.db.cursor.execute("INSERT INTO passwords (user_id, website, username, password) VALUES (?,?,?,?)",
                               (user_id, website, username, encrypted_passwords))
        self.db.conn.commit()

    def get_passwords(self, user_id):
        self.db.cursor.execute("SELECT id, website, username, password FROM passwords WHERE user_id= ?", (user_id,))
        encrypted_passwords = self.db.cursor.fetchall()
        return [(id, website, username, self.db.decrypt_password(password)) for id, website, username, password in encrypted_passwords] 

    def update_password(self, password_id, website, username, password):
        encrypted_password = self.db.encrypt_password(password)
        self.db.cursor.execute("UPDATE passwords SET website = ?, username = ?, password = ? WHERE id = ?",
                               (website, username, encrypted_password, password_id))
        self.db.conn.commit()

    def delete_password(self, password_id):
        self.db.cursor.execute("DELETE FROM passwords WHERE id = ?", (password_id,))
        self.db.conn.commit()
