import os

class DirectoryManager:
    path = ""
    dirContents = []

    def __init__(self, path):
        self.path = path
        
    def getDirContents(self):
        for item in os.listdir(self.path):
            self.dirContents.append(os.path.splitext(item)[0])
    
    def getFileContents(self):
        for item in os.listdir(self.path):
            self.dirContents.append(os.path.splitext(item)[0])