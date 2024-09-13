import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from backend.database import Database, User

def test_login():
    db = Database(db_file="test_safeKeeper.db")  # Use a separate test database
    user = User(db)
    
    # Try to register the user (this will fail if the user already exists)
    registration_result = user.register("OCHHQ", "12345")
    print(f"Registration result: {registration_result}")
    
    # Now, let's try to login
    login_result = user.login("OCHHQ", "12345")
    print(f"Login result: {login_result}")

    db.close()

if __name__ == "__main__":
    test_login()