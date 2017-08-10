from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.uix.widget import Widget
from kivy.graphics import Line


class Painter(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]


class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("kivy_pic.kv")

class MainApp(App):

    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()




















# from kivy.app import App
# from kivy.lang import Builder
#
# presentation = Builder.load_file("kivy_pic.kv")
#
# class MainApp(App):
#
#     def build(self):
#         return presentation
#
#
# if __name__ == "__main__":
#
#     MainApp().run()
#
#
#
#








































# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.graphics import Line
#
# class DrawInput(Widget):
#
#     def on_touch_down(self, touch):
#         print(touch)
#         with self.canvas:
#             touch.ud["line"] = Line(points=(touch.x, touch.y))
#
#     def on_touch_move(self, touch):
#         print(touch)
#         touch.ud["line"].points += (touch.x, touch.y)
#
#     def on_touch_up(self, touch):
#         print("RELEASED!",touch)
#
#
# class SimpleKivy4(App):
#
#     def build(self):
#         return DrawInput()
#
# if __name__ == "__main__":
#     SimpleKivy4().run()


























# class LoginScreen(GridLayout):
#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text="Username:"))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#
#         self.add_widget(Label(text="Password:"))
#         self.password = TextInput(multiline=False, password=True)
#         self.add_widget(self.password)
#
#         self.add_widget(Label(text="Two Factor Auth:"))
#         self.tfa = TextInput(multiline=False)
#         self.add_widget(self.tfa)
#
#
# class TestApp(App):
#     def build(self):
#         return LoginScreen()
#
# TestApp().run()
