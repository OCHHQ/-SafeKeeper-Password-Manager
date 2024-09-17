import tkinter as tk
from tkinter import ttk, messagebox
from ui.components import LoginScreen, PasswordListView, AddEditPasswordForm
from PIL import Image, ImageTk
from backend.database import Database, User
import os

class Safekeeper(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("safekeeper password manager")
        self.geometry("700x500")
        self.db = Database()
        self.user = User(self.db)
        self.current_user = None
        self.current_user_id = None
        self.create_widgets()
        
    def create_widgets(self):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the path to the assets folder
        assets_dir = os.path.join(script_dir, 'assets')
        
        # Construct the full path to the background image
        bg_image_path = os.path.join(assets_dir, 'background_image.png')
        
        # Print the full path for debugging
        print(f"Looking for background image at: {bg_image_path}")
        if os.path.exists(bg_image_path):
        # Load the image
            try:
                image = Image.open(bg_image_path)
                image = image.resize((700, 500), Image.LANCZOS)
                self.background_image = ImageTk.PhotoImage(image)

                # Create a label with image
                self.background_label = tk.Label(self, image=self.background_image)
                self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            except FileNotFoundError:
                print(f"Background image not found at {bg_image_path}")
                # Optionally, create a plain background if the image is not found
                self.configure(bg='#f0f0f0')

        #here after thoughtul research we create a frame to hold content at the middle
        self.content_frame = tk.Frame(self, bg="#1A5F7A", bd=5)
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.login_screen = LoginScreen(self.content_frame, login_callback=self.on_login, register_callback=self.on_register)
        self.login_screen.pack(padx=20, pady=20) 

        #successful login
        self.password_list = PasswordListView(self.content_frame,
                                              add_callback=self.show_add_password_form,
                                              edit_callback=self.show_add_password_form,
                                              delete_callback=self.delete_password)
        self.password_list.pack_forget()

        #creating a logout button(hidden initally)
        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack_forget()


    def on_login(self, username, password, user_id):
        if self.user.login(username, password):
            self.current_user = username
            self.current_user_id = user_id
            self.login_screen.pack_forget()
            self.password_list.pack(expand=True, fill='both', padx=20, pady=20)
            self.logout_button.pack(side='bottom', pady=10)
            self.load_passwords()
        else:
            messagebox.showerror("Login failied", "invalid username or password")

    def on_register(self, username, password):
        if self.user.register(username, password):
            messagebox.showinfo("Registration successful", "you can now login with your new account ")
        else:
            messagebox.showerror("Registarion failed", "Username already exists")

    def show_add_password_form(self):
        AddEditPasswordForm(self, callback=self.add_password)

    def show_edit_password_form(self):
        selected_item = self.password_list.get_selected_item()
        if selected_item:
            AddEditPasswordForm(self, callback=self.update_password, initial_values=selected_item)
        else:
            messagebox.showwarning("No Selecteion", "please select a password to edit")

    def add_password(self, website, username, password):
        password_id = self.user.add_password(self.current_user_id, website, username, password)
        self.password_list.add_password(password_id, website, username, password)
        self.load_passwords()
        messagebox.showinfo("Success", f"Password for {website} added successfully!")

    def load_passwords(self):
        passwords = self.user.get_passwords(self.current_user_id)
        self.password_list.load_passwords(passwords)


    def update_password(self, website, username, password):
        selected_item = self.password_list.get_selected_item()
        if selected_item:
            password_id = selected_item[0]
            self.user.update_password(password_id, website, username, password)
            self.load_passwords()
            messagebox.showinfo("Success", f"password for {website} updated successfully!")

    def delete_password(self):
        selected_item = self.password_list.get_selected_item()
        if selected_item:
            password_id = selected_item[0]
            website = selected_item[1]
            if messagebox.askyesno("Confirm deletion", f"Are you sure you want to delete the password for {website}?"):
                self.user.delete_password(password_id)
                self.load_passwords()
                messagebox.showinfo("Success", f"password for {website} deleted successfully!")
        else:
            messagebox.showwarning("No Selection", "please select a password to delete")


    def logout(self):
        self.current_user = None
        self.current_user_id = None
        self.password_list.clear_passwords()
        self.password_list.pack_forget()
        self.logout_button.pack_forget()
        self.login_screen.pack(padx=20, pady=20)
        self.login_screen.username_entry.delete(0, tk.END)
        self.login_screen.password_entry.delete(0, tk.END)

   


def main():
    app = Safekeeper()
    app.mainloop()

if __name__ == "__main__":
    main()