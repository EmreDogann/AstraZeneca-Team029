import os

class DirectoryManager:
    path = ""
    dirContents = []

    def __init__(self, path):
        self.path = path
        
    def getDirContents(self):
        for item in os.listdir(self.path):
            # self.dirContents.append(os.path.splitext(item)[0])
            self.dirContents.append(item)
    
    def renameDir(self, oldName, newName):
        os.rename(os.path.join(self.path, oldName), os.path.join(self.path, newName))

    def getFileContents(self):
        words = []
        with open (self.path, 'rt') as myFile:
            for line in myFile:
                words.append()
                print(line)
        # print(contents)