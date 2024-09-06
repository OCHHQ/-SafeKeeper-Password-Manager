import tkinter as tk
from ui.components import LoginScreen, PasswordListView, AddEditPasswordForm

class safekeeper(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("safekeeper password manager")
        self.geometry("400x400")
        self.current_user = None
        self.create_widgets()
        
    def create_widgets(self):
        self.logo = tk.PhotoImage(file="src/assets/lock_image.png")
        self.logo = self.logo.subsample(4,4)
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.pack(pady=10)

        self.login_screen = LoginScreen(self, login_callback=self.on_login)
        self.login_screen.pack(expand=True, fill='both')

        #successful login
        self.password_list = PasswordListView(self)
        self.password_list.add_button.config(command=self.show_add_edit_form)
        self.password_list.pack_forget()

        #for now the switch between views
        self.switch_button = tk.Button(self, text="switch view", command=self.switch_view)
        self.switch_button.pack(side='bottom', pady=10)

    def switch_view(self):
        if self.login_screen.winfo_viewable():
            self.login_screen.pack_forget()
            self.password_list.pack(expand=True, fill='both')
        else:
            self.password_list.pack_forget()
            self.login_screen.pack(expand=True, fill='both')

    def on_login(self, username):
        self.current_user = username
        self.login_screen.pack_forget()
        self.password_list.pack(expand=True, fill='both')

    def show_add_edit_form(self):
        add_edit_form = AddEditPasswordForm(self, callback=self.add_password)
        add_edit_form.grab_set()

    def add_password(self, website, username, password):
        self.password_list.add_password(website, username, password)
        print("Password added and list refreshed")      


def main():
    app = safekeeper()
    app.mainloop()

if __name__ == "__main__":
    main()