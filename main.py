from DirectoryManager import DirectoryManager
from FileSpellChecker import FileSpellChecker
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.utils import get_color_from_hex as hex
import tkinter
from tkinter import filedialog
import os
Window.clearcolor = (1,1,1,1)

# path =r"C:\Users\Emre\Downloads\GitHub\testDir\test.txt" 

class HomeScreen(Widget):
    fileImg1 = ObjectProperty(None)
    fileImg2 = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos = self.on_mouse_pos)
        self.tkinterRoot = tkinter.Tk()
        self.tkinterRoot.withdraw()
        self.path = ''

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
        self.path = filedialog.askopenfile(parent=self.tkinterRoot, initialdir="./", title='Please select a file').name
        if (self.path != None):
            self.fileImport("File")

    def on_mouse_pos(self, window, pos):
        if ((window.mouse_pos[0]/window.size[0]) < 0.5):
            self.fileImg1.color = hex("#a6a6a6")
            self.fileImg2.color = hex("#c9c9c9")
        else:
            self.fileImg1.color = hex("#c9c9c9")
            self.fileImg2.color = hex("#a6a6a6")
        

class FileNameScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):

    def build(self):
        # Binding the drop file
        Window.bind(on_dropfile=self._on_file_drop)
        Window.bind(on_cursor_enter=lambda *__: Window.show())
        self.homeScreen = HomeScreen()
        return self.homeScreen

    def _on_file_drop(self, window, file_path):
        self.homeScreen.path = file_path.decode("utf-8")
        if ((window.mouse_pos[0]/window.size[0]) < 0.5):
            if (os.path.isdir(self.homeScreen.path)):
                self.homeScreen.fileImport("Directory")
            else:
                fileImg1_animation = Animation(color=hex("#c93838"), duration=0.0) + Animation(color=hex("#c93838"), duration=0.5) + Animation(color=self.homeScreen.fileImg1.color, duration=2.0)
                fileImg1_animation.start(self.homeScreen.fileImg1)
                self.homeScreen.fileImg1.color = hex("#c9c9c9")
        else:
            if (os.path.isfile(self.homeScreen.path)):
                self.homeScreen.fileImport("File")
            else:
                fileImg2_animation = Animation(color=hex("#c93838"), duration=0.0) + Animation(color=hex("#c93838"), duration=0.5) + Animation(color=self.homeScreen.fileImg2.color, duration=2.0)
                fileImg2_animation.start(self.homeScreen.fileImg2)
                self.homeScreen.fileImg2.color = hex("#c9c9c9")


if __name__ == '__main__':
    MainApp().run()