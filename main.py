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

    def fileImport(self, operationType):
        self.directoryManager = DirectoryManager(r"C:\Users\Emre\Downloads\GitHub\testDir\abuizgai.txt")
        if (operationType == "Directory"):
            self.directoryManager.getDirContents()
        elif (operationType == "Deep"):
            self.directoryManager.getFileContents()
    
    def fileRename(self, operationType):
        if (operationType == "DirectoryRename"):
            self.directoryManager.renameDir(self.directoryManager.dirContents[0], "abuizgai.txt")
        elif (operationType == "Deep"):
            self.directoryManager.getFileContents()

class FileNameScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show(self, dt):
        print("hi")

class MainApp(App):
    def build(self):
        mainScreen = MainScreen()
        mainScreen.fileImport("Deep")
        # mainScreen.fileRename("Deep")
        return mainScreen


if __name__ == '__main__':
    MainApp().run()