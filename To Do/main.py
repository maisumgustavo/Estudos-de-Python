from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyLayout(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    App().run()
