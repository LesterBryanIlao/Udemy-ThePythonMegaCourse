from pathlib import Path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
import json
from datetime import datetime
import random
import glob

Builder.load_file('design.kv')


class LoginScreen(Screen):

    def sign_up(self):
        self.manager.current = "signup_screen"

    def login(self, username, password):
        username = username.strip()
        password = password.strip()
        with open("users.json") as file:
            users = json.load(file)
        if username in users and users[username]["password"] == password:
            self.manager.current = "login_screen_success"
        else:
            # self.manager.current = "login_screen"
            self.ids.login_wrong.text = "Wrong username or password!"


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

    def random_line(self, filename):
        with open(f"quotes/{filename}.txt", 'r', encoding='cp850') as f:
            quote = f.readlines()
            return random.choice(quote).strip()

    def get_quote(self):
        feeling_strip = self.ids.feeling.text.strip().lower()

        available_feelings = glob.glob("quotes/*txt")

        available_feelings = [
            Path(filename).stem for filename in available_feelings]

        self.ids.enlighten_me.text = self.random_line(
            feeling_strip) if feeling_strip in available_feelings else "Not in the selection. Try again."


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
