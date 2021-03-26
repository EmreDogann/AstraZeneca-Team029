from DirectoryManager import DirectoryManager
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class HomeScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def fileImport(self, operationType):
        self.directoryManager = DirectoryManager(r"C:\Users\Emre\Downloads\GitHub\testDir\test.txt")
        if (operationType == "Directory"):
            self.directoryManager.getDirContents()
        elif (operationType == "Deep"):
            self.words = self.directoryManager.getFileContents()
    
    def fileRename(self, operationType):
        if (operationType == "DirectoryRename"):
            self.directoryManager.renameDir(self.directoryManager.dirContents[0], "test2.txt")
        elif (operationType == "Deep"):
            self.directoryManager.createNewFile(self.words)

class FileNameScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show(self, dt):
        print("hi")

class MainApp(App):
    def build(self):
        homeScreen = HomeScreen()
        # mainScreen.fileImport("Deep")
        # mainScreen.fileRename("Deep")
        # mainScreen.changeFileContents("Deep")
        return homeScreen


if __name__ == '__main__':
    MainApp().run()