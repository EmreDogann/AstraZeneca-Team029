import tkinter
from tkinter import filedialog
tkinterRoot = tkinter.Tk()
tkinterRoot.withdraw()
# Fixing Tkinter mac: create the tkinter window first
#       https://stackoverflow.com/questions/42673733/nsexception-in-kivy-with-matplotlib-and-tkinter/42674522#42674522


class DialogueWindow:

    def __init__(self):
        self.helloWorld = 'hellow'
        

    def openDialogue(self, type):

        if(type == 'File'):
            return filedialog.askopenfile(parent=tkinterRoot, initialdir="./", title='Please select a file')
        elif(type == 'Directory'):
            return filedialog.askdirectory(parent=tkinterRoot, initialdir="./", title='Please select a directory')
        else:
            print("ERROR: SOMETHING WENT WRONG.aum")

