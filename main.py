from DirectoryManager import DirectoryManager
from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.graphics.texture import Texture
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class MainScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def FileRename(self):
        self.directoryManager = DirectoryManager("C:/Users/Emre/Downloads/GitHub")
        if (self.type == "DirectoryRename"):
            self.directoryManager.getDirContents()
        else:
            self.directoryManager.getFileContents()
        

class FileNameScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show(self, dt):
        print("hi")

class MainApp(App):
    def build(self):
        mainScreen = MainScreen()
        mainScreen.FileRename()
        return mainScreen


if __name__ == '__main__':
    MainApp().run()