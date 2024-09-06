import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

USER_FILE = 'user.json'


def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = generate_password_hash(password)
    save_users(users)
    return True

def authenticate_user(username, password):
    users = load_users()
    if username in users and check_password_hash(users[username], password):
        return True
    return False