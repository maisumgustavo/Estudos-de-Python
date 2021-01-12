from kivy.app import App
from kivy.uix.widget import Widget

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyLayout()

MyApp().run()