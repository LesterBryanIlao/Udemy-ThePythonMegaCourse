from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
import json
from datetime import datetime

Builder.load_file('design.kv')


class LoginScreen(Screen):

    def sign_up(self):
        self.manager.current = "signup_screen"

    def login(self, username, password):
        username = username.strip()
        password = password.strip()
        with open("users.json") as file:
            users = json.load(file)
        if username in users:
            if users[username]["password"] == password:
                self.manager.current = "login_screen_success"
            else:
                self.manager.current = "login_screen"
        else:
            self.manager.current = "login_screen"


class SignUpScreen(Screen):
    def submit(self):
        self.manager.current = "login_screen"

    def add_user(self, username, password):
        username = username.strip()
        password = password.strip()

        # Read jason file
        with open("users.json") as file:
            users = json.load(file)

        users[username] = {"username": username,
                           "password": password,
                           "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        # Rewrite json file
        with open('users.json', 'w') as file:
            json.dump(users, file)

        self.manager.current = "signup_screen_success"

    def cancel(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class SignUpScreenSuccess(Screen):
    def go_to_login_page(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
