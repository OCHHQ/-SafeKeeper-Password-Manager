import tkinter as tk
from tkinter import ttk, messagebox
from backend.database import User, Database

class LoginScreen(tk.Frame):
    def __init__(self,master=None, login_callback=None, register_callback = None):
        super().__init__(master)
        self.master=master
        self.login_callback = login_callback
        self.register_callback = register_callback
        self.db = Database()
        self.user = User(self.db)
        self.create_widgets()
    
    def create_widgets(self):
        self.username_label =tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self, text="password")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, pady=10, )

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.grid(row=2, column=1, pady=10, )

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user.login(username, password):
            user_id = self.user.get_user_id(username)
            messagebox.showinfo("Login successfully", f"welcome {username}!")
            if self.login_callback:
                self.login_callback(username, password, user_id)
        else:
            messagebox.showerror("Login failed", "invailed username or password")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showerror("Registeration Failed", "Username and password cannot be empty")
        elif self.user.register(username, password):
            messagebox.showinfo("Registeration successful", "User Registration Successfully!")
        else:
            messagebox.showerror("Registarion failed", "username already exists")



class PasswordListView(tk.Frame):
    def __init__(self, master=None, add_callback=None, edit_callback=None, delete_callback=None):
        super().__init__(master)
        self.master = master
        self.add_callback = add_callback
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback
        self.create_widgets()
        self.passwords = []

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=('ID','Website', 'Username', 'Password'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Website', text='Website')
        self.tree.heading('Username', text='Username')
        self.tree.heading('Password', text='Password')
        self.tree.column('ID', width=50)
        self.tree.column('Website', width=150)
        self.tree.column('Username', width=150)
        self.tree.column('Password', width=500)
        self.tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.tree.configure(yscroll=scrollbar.set)

        self.add_button = tk.Button(self, text="Add Password", command=self.add_callback)
        self.add_button.grid(row=1, column=0, pady=10)

        self.edit_button = tk.Button(self, text="Edit password", command=self.edit_callback)
        self.edit_button.grid(row=1, column=1, padx=10)

        self.delete_button = tk.Button(self, text="Delete password", command=self.delete_callback)
        self.delete_button.grid(row=1, column=2, padx=10)

    def load_passwords(self, passwords):
        self.passwords = passwords
        self.refresh_list()

    
    def get_selected_item(self):
        selection = self.tree.selection()
        if selection:
            return self.tree.item(selection[0])["values"]
        return None
    
    def add_password(self,password_id, website, username, password):
        self.passwords.append((password_id, website, username, password))
        self.refresh_list()

    def clear_passwords(self):
        self.passwords = []
        self.refresh_list()

    def refresh_list(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for password in self.passwords:
            self.tree.insert('', "end", values=password)


    




class AddEditPasswordForm(tk.Toplevel):
    def __init__(self, master=None, callback= None, initial_values= None):
        super().__init__(master)
        self.title("Add/edit password")
        self.callback = callback
        self.initial_values = initial_values
        self.create_widgets()

    def create_widgets(self):
        self.website_label = tk.Label(self, text="Website:")
        self.website_label.grid(row=0, column=0, padx=5, pady=5)
        self.website_entry = tk.Entry(self)
        self.website_entry.grid(row=0, column=1, padx=5, pady=5)

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=1, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=2, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        self.save_button = tk.Button(self, text="Save", command=self.save_password)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)

        if self.initial_values:
            self.website_entry.insert(0, self.initial_values[1])
            self.username_entry.insert(0, self.initial_values[2])
            self.password_entry.insert(0, self.initial_values[3])

    def save_password(self):
            website = self.website_entry.get()
            username = self.username_entry.get()
            password = self.password_entry.get()
            if website and username and password:
                if self.callback:
                    self.callback(website, username, password)
                self.destroy()
            else:
                messagebox.showerror("Error", "All fields are required")


