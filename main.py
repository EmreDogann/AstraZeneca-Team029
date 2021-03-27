from DirectoryManager import DirectoryManager
from FileSpellChecker import FileSpellChecker
from DialogueWindow import DialogueWindow
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.uix.recycleview import RecycleView
from kivy.utils import get_color_from_hex as hex
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
Window.clearcolor = (1,1,1,1)

# Global store.
directoryManager = DirectoryManager()

class HomeScreen(Screen):
    fileImg1 = ObjectProperty(None)
    fileImg2 = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize TKinter
        self.dialogueWindow = DialogueWindow()

        # Bind mouse movement event - Used for the on-hover effects.
        Window.bind(mouse_pos = self.on_mouse_pos)
        self.path = ''

    # Used to retreive directory/file contents once the path has been supplied.
    def fileImport(self, operationType):
        directoryManager.path = self.path
        if (operationType == "Directory"):
            directoryManager.getDirContents()

        elif (operationType == "File"):
            self.words = directoryManager.getFileContents()

    # Called when folder is manually selected
    def onFolderButtonPressed(self):
        self.path = self.dialogueWindow.openDialogue('Directory')
        if (self.path != ""):
            self.fileImport("Directory")
            self.fileSpellChecker = FileSpellChecker(directoryManager.dirContents)
            
            result = self.fileSpellChecker.spellCheck()

            misspelledWords = []
            suggestions = []
            for index, x in enumerate(result):
                misspelledWords.append({'text': x[0]+x[1]})
                suggestions.append({'text': str(index) + ": " + x[2][0]})

            directoryManager.suggestions = result

            spellChecker = self.manager.get_screen('spellCheckerScreen')
            spellChecker.misspelledWords.data = misspelledWords
            spellChecker.suggestions.data = suggestions
            spellChecker.folderName.text = os.path.splitext(directoryManager.path)[0]

            self.manager.current = "spellCheckerScreen"
            self.manager.transition.direction = "left"

    # Called when file is manually selected
    def onFileButtonPressed(self):
        self.path = self.dialogueWindow.openDialogue('File')

        if (self.path != None):
            self.path = self.path.name
            self.fileImport("File")

            self.manager.current = "spellCheckerScreen"
            self.manager.transition.direction = "left"

    # on_hover effects
    def on_mouse_pos(self, window, pos):
        if ((window.mouse_pos[0]/window.size[0]) < 0.5):
            self.fileImg1.color = hex("#a6a6a6")
            self.fileImg2.color = hex("#c9c9c9")

        else:
            self.fileImg1.color = hex("#c9c9c9")
            self.fileImg2.color = hex("#a6a6a6")

# New screen for listing word corrections
class SpellCheckerScreen(Screen):
    folderName = ObjectProperty(None)
    misspelledWords = ObjectProperty(None)
    suggestions = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# Base manager class which handles switching between pages.
class Manager(ScreenManager):
    homeScreen = ObjectProperty(None)
    spellCheckerScreen = ObjectProperty(None)

# Custom widget with an on_press event (correctSpelling) which will correct the spelling for the folder selected.
class ListButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def correctSpelling(self):
        index = int(self.text.split(': ')[0])
        directoryManager.renameDir(directoryManager.suggestions[index][0] + directoryManager.suggestions[index][1], directoryManager.suggestions[index][2][0] + directoryManager.suggestions[index][1])

        

class MainApp(App):

    def build(self):
        # Binding the drop file
        Window.bind(on_dropfile=self._on_file_drop)
        # Detects when mouse has entered window and focuses window as a result
        Window.bind(on_cursor_enter=lambda *__: Window.show())

        # Setup manager class.
        self.manager = Manager(transition=SlideTransition())

        return self.manager

    # Called when file drop detected.
    def _on_file_drop(self, window, file_path):
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