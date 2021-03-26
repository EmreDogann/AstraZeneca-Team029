from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.graphics.texture import Texture
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class MainScreen(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show(self, dt):
        print("hi")

class MainApp(App):
    def build(self):
        mainScreen = MainScreen()
        return mainScreen


if __name__ == '__main__':
    MainApp().run()