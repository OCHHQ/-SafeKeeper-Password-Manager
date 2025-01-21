# SafeKeeper Password Manager

SafeKeep Password Manager is a desktop application designed to securely store and manage passwords for various websites and services. It aims to simplify the process of managing multiple accounts while prioritizing security and usability.

🚀 Project Overview
SafeKeep Password Manager was born out of a need to provide an intuitive, secure, and user-friendly password management solution for individuals. The goal of the project was not only to implement basic password storage but to also include features like password encryption, password generation, and user authentication.
# 🚀 Project Overview

This project is a part of my portfolio, showcasing my skills in Python, GUI development (Tkinter), and secure storage management. Throughout the development, I faced numerous technical challenges, ranging from designing a user-friendly interface to implementing robust security measures.


# Features (Planned)
1.Secure Storage: Uses encryption algorithms to securely store passwords.
2.User Authentication: Allows users to register, log in, and manage their accounts.
3.Password Generation: Provides strong, randomly generated passwords.
4.Password Strength Indicator: Visual feedback on the strength of passwords.
5.CRUD Operations: Add, edit, delete, and view saved passwords.
6.Responsive UI: Designed using Tkinter to ensure a smooth and user-friendly experience.

#💡 Inspiration & Motivation
I started SafeKeep with the goal of solving a common problem: the need to remember multiple strong passwords. Inspired by tools like LastPass and 1Password, I wanted to build a more tailored solution, learning the technicalities behind encryption, security, and user experience.

During development, one of my main challenges was implementing bcrypt for password hashing and salting. I wanted to ensure that even if someone accessed the database, they wouldn't be able to retrieve user passwords easily.

Another challenge was in creating a dynamic and scalable UI in Tkinter, a tool I was relatively new to. Ensuring the responsiveness of various elements like forms, password lists, and pop-up windows required careful thought and refinement.

# Technologies Used
1.Language: Python 3.12
2.Libraries: Tkinter, bcrypt, sqlite3, hashlib
3.Database: SQLite (local storage)
4.Security: Bcrypt for password hashing and encryption
5.Development Environment: Git Bash, VSCode, Git for version control

# project structure 
SafeKeeper-Password-Manager/
├── doc/
├── src/
│   ├── assets/
│   │   └── lock_image.png
│   ├── backend/
│   │   ├── init.py
│   │   └── user_auth.py
│   ├── ui/
│   │   ├── pycache/
│   │   │   └── components.cpython-311.pyc
│   │   └── components.py
│   ├── uiclear/
│   └── main.py
├── tests/
│   └── init.py
├── venv/
├── README.md
└── requirements.txt
main.py: The entry point of the application that initializes the UI and backend.
backend: Handles database operations and encryption logic.
ui: Contains the UI components, including the Login Screen, Password List View, and Add/Edit Form.
assets: Houses all images used in the project, including logos and background images.
tests: Contains unit tests for key functionality.

#Screenshots

Login Screen

Password List View

# Security & Encryption

SafeKeep Password Manager uses bcrypt to ensure that user passwords are stored securely. When a user registers or updates a password, it is hashed and salted using bcrypt before being stored in the SQLite database. This ensures that even if the database is compromised, raw passwords are not exposed.
import bcrypt

# Example of password hashing with bcrypt
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

Additionally, the application uses an encryption key stored locally for securing passwords during storage and retrieval. This ensures that passwords stored in the database are never stored in plaintext.

# Challenges & Learnings

Database Schema Design
One of the early technical challenges was designing a flexible database schema that allowed for secure storage and quick retrieval of user data. I opted for SQLite for its simplicity, but had to ensure that sensitive data (like passwords) was properly encrypted.

# UI Challenges with Tkinter
Creating a responsive and user-friendly UI in Tkinter presented its own set of challenges. Tkinter, while powerful for simple interfaces, required a lot of fine-tuning to ensure that elements like tables and forms resized properly based on window dimensions.

# Next Iteration
In future iterations, I envision integrating cloud-based storage to allow users to securely sync their passwords across multiple devices. Additionally, improving the UI with modern frameworks like PyQt or Kivy could provide a more polished experience.

 # Timeline
Week 1: Set up project structure, implemented basic UI and user registration system.
Week 2: Added password encryption, implemented password storage and retrieval.
Week 3: Refined the UI, added password generation and strength checking.
Week 4: Bug fixes, user testing, and README documentation.

# Future Improvements

Cloud Sync: Allow users to sync their passwords across devices.
2FA Integration: Add two-factor authentication for added security.
Mobile Version: Build a mobile version using frameworks like Kivy.
UI Overhaul: Migrate from Tkinter to PyQt for a more modern look and feel.

# How to Use

Clone the repository:
git clone https://github.com/ochhq/SafeKeep-Password-Manager.git

Navigate to the project directory:

cd SafeKeep-Password-Manager

Install dependencies:
pip install -r requirements.txt

Run the application:

python src/main.py



# Contributing
Contributions are welcome! If you have ideas for improvement or want to fix a bug, feel free to open a pull request or submit an issue. Let's make SafeKeep even better!

# License
This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

- Thanks to ALX who as helped shape and craft my SafeKeeper.
- Special thanks to the Python and Tkinter communities for their excellent documentation and resources.

# Contributor
### Chiba Ismail
Email: ismailchiba0@gmail.com
github: ismailchiba

### Enoseje Collins
Email: enosejecollins@gmail.com
github: OCHHQ

### Onyinyechi Nwaneri
Email: onyinychinwaneri@gmail.com
github: onyii-e

### Obah Edwin
Email: obahedwin@ymail.com
github: Babaoni147
