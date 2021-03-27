from DirectoryManager import DirectoryManager
from FileSpellChecker import FileSpellChecker
from DialogueWindow import DialogueWindow
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Canvas, Color
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.uix.recycleview import RecycleView
from kivy.utils import get_color_from_hex as hex
# import tkinter
# from tkinter import filedialog
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
Window.clearcolor = (1,1,1,1)

# path =r"C:\Users\Emre\Downloads\GitHub\testDir\test.txt" 

class HomeScreen(Screen):
    fileImg1 = ObjectProperty(None)
    fileImg2 = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialogueWindow = DialogueWindow()

        Window.bind(mouse_pos = self.on_mouse_pos)
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
        self.path = self.dialogueWindow.openDialogue('Directory')
        if (self.path != ""):
            self.fileImport("Directory")
            self.fileSpellChecker = FileSpellChecker(self.directoryManager.dirContents)
            
            spellChecker = self.manager.get_screen('spellCheckerScreen')
            misspelledWords = []
            suggestions = []
            for x in self.fileSpellChecker.spellCheck():
                misspelledWords.append({'text': x[0]+x[1]})
                suggestions.append({'text': x[2][0]})
            print(suggestions)
            spellChecker.misspelledWords.data = misspelledWords
            spellChecker.suggestions.data = suggestions


            self.manager.current = "spellCheckerScreen"
            self.manager.transition.direction = "left"

    def onFileButtonPressed(self):
        self.path = self.dialogueWindow.openDialogue('File')

        if (self.path != None):
            self.path = self.path.name
            self.fileImport("File")

            self.manager.current = "spellCheckerScreen"
            self.manager.transition.direction = "left"

    def on_mouse_pos(self, window, pos):
        if ((window.mouse_pos[0]/window.size[0]) < 0.5):
            self.fileImg1.color = hex("#a6a6a6")
            self.fileImg2.color = hex("#c9c9c9")

        else:
            self.fileImg1.color = hex("#c9c9c9")
            self.fileImg2.color = hex("#a6a6a6")

class SpellCheckerScreen(Screen):
    misspelledWords = ObjectProperty(None)
    suggestions = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Manager(ScreenManager):
    homeScreen = ObjectProperty(None)
    spellCheckerScreen = ObjectProperty(None)

class ListButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def correctSpelling(self):
        self.background_color = hex('#65d656')
        # with self.canvas:
        #     Color(rgba=(101/255, 214/255, 86/255, 1))

class MainApp(App):

    def build(self):
        # Binding the drop file
        Window.bind(on_dropfile=self._on_file_drop)
        Window.bind(on_cursor_enter=lambda *__: Window.show())

        self.manager = Manager(transition=SlideTransition())

        return self.manager

    def _on_file_drop(self, window, file_path):
        if (self.manager.current == "homeScreen"):
            homeScreen = self.manager.get_screen('homeScreen')
            homeScreen.path = file_path.decode("utf-8")
            if ((window.mouse_pos[0]/window.size[0]) < 0.5):
                if (os.path.isdir(homeScreen.path)):
                    homeScreen.fileImport("Directory")
                    self.manager.current = "spellCheckerScreen"
                    self.manager.transition.direction = "left"

                else:
                    fileImg1_animation = Animation(color=hex("#c93838"), duration=0.0) + Animation(color=hex("#c93838"), duration=0.5) + Animation(color=homeScreen.fileImg1.color, duration=2.0)
                    fileImg1_animation.start(homeScreen.fileImg1)
                    homeScreen.fileImg1.color = hex("#c9c9c9")

            else:
                if (os.path.isfile(homeScreen.path)):
                    homeScreen.fileImport("File")
                    self.manager.current = "spellCheckerScreen"
                    self.manager.transition.direction = "left"

                else:
                    fileImg2_animation = Animation(color=hex("#c93838"), duration=0.0) + Animation(color=hex("#c93838"), duration=0.5) + Animation(color=homeScreen.fileImg2.color, duration=2.0)
                    fileImg2_animation.start(homeScreen.fileImg2)
                    homeScreen.fileImg2.color = hex("#c9c9c9")


if __name__ == '__main__':
    MainApp().run()