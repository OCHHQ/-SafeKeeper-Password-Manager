# SafeKeeper Password Manager

SafeKeeper is a secure, user-friendly password manager built with Python and Tkinter.

# Features (Planned)
user registeation and authentication
Secure password storage
Password generation
User-friendly GUI
Encryption of sensitive data

# Setup

Clone the repository:
bash
git clone https://github.com/OCHHQ/safekeeper.git
cd safekeeper-password-manager
source venv/Scripts/activate
intall dependancy

# usage

when you first run the application, you will see a login screen
if you're a new user, enter a username and password , then click "register"
once registered, you wil be able to login  your credentails 
after logging in , you will see the main password list view (currently a placeholder)
you can add new passwords using the "Add password" button (functionality to be implemented )

# development

we use git for version control.
follow pep 8 style guideline for python code.
write unit tests for new features

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

# Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- Thanks to all contributors who have helped shape SafeKeeper.
- Special thanks to the Python and Tkinter communities for their excellent documentation and resources.