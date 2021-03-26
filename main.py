from DirectoryManager import DirectoryManager
from FileSpellChecker import FileSpellChecker
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
import tkinter
from tkinter import filedialog
Window.clearcolor = (1,1,1,1)

# path =r"C:\Users\Emre\Downloads\GitHub\testDir\test.txt" 

class HomeScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tkinterRoot = tkinter.Tk()
        self.tkinterRoot.withdraw()
        self.path = ''
        # Window.bind(mouse_pos = lambda w, p: setattr(self.label, 'text', str(p)))


    def fileImport(self, operationType):
        self.directoryManager = DirectoryManager(self.path)
        if (operationType == "Directory"):
            self.directoryManager.getDirContents()
        elif (operationType == "File"):
            self.words = self.directoryManager.getFileContents()

    
    def fileRename(self, operationType):
        if (operationType == "Directory"):
            self.directoryManager.renameDir(self.directoryManager.dirContents[0], "test2.txt")
        elif (operationType == "File"):
            self.directoryManager.createNewFile(self.words)

    def onFolderButtonPressed(self):
        self.path = filedialog.askdirectory(parent=self.tkinterRoot, initialdir="./", title='Please select a directory')
        if (self.path != ""):
            self.fileImport("Directory")
        # self.fileSpellChecker = FileSpellChecker(self.directoryManager.dirContents)
        # print(self.fileSpellChecker.spellCheck())

    def onFileButtonPressed(self):
        self.path = filedialog.askopenfile(parent=self.tkinterRoot, initialdir="./", title='Please select a file')
        if (self.path != ""):
            self.fileImport("File")
    
    # def on_touch_up(self, touch):
    #     print("Mouse UP X", touch.spos[0])
    #     # self.btn.opacity = 1
        

class FileNameScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):

    def build(self):
        # Binding the drop file
        Window.bind(on_dropfile=self._on_file_drop)
        self.homeScreen = HomeScreen()
        return self.homeScreen

    def _on_file_drop(self, window, file_path):
        self.homeScreen.path = file_path.decode("utf-8")
        mouse_x = window.mouse_pos[0]/window.size[0]
        if (mouse_x < 0.5):
            self.homeScreen.fileImport("Directory")
        else:
            self.homeScreen.fileImport("File")


if __name__ == '__main__':
    MainApp().run()