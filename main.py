from DirectoryManager import DirectoryManager
from FileSpellChecker import FileSpellChecker
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
import platform
Window.clearcolor = (1, 1, 1, 1)

# path =r"C:\Users\Emre\Downloads\GitHub\testDir\test.txt" 

class HomeScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.path = ''


    def fileImport(self, operationType):
        self.directoryManager = DirectoryManager(self.path)
        if (operationType == "Directory"):
            self.directoryManager.getDirContents()
        elif (operationType == "Deep"):
            self.words = self.directoryManager.getFileContents()

    
    def fileRename(self, operationType):
        if (operationType == "Directory"):
            self.directoryManager.renameDir(self.directoryManager.dirContents[0], "test2.txt")
        elif (operationType == "Deep"):
            self.directoryManager.createNewFile(self.words)

    def onFileFolderButtonPressed(self):
        self.fileImport("Directory")
        self.fileSpellChecker = FileSpellChecker(self.directoryManager.dirContents)
        print(self.fileSpellChecker.spellCheck())
        

class FileNameScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show(self, dt):
        print("hi")

class MainApp(App):

    def build(self):
        # binding the drop file 
        Window.bind(on_dropfile=self._on_file_drop)
        
        self.homeScreen = HomeScreen()

        return self.homeScreen

    def _on_file_drop(self, window, file_path):
        self.homeScreen.path = file_path.decode("utf-8")
        return


if __name__ == '__main__':
    MainApp().run()