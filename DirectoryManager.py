import os

class DirectoryManager:
    path = ""
    dirContents = []
    newLineIndies = set()
    suggestions = []

    def __init__(self):
        pass
    
    def setPath(self, path):
        self.path = path
        
    def getDirContents(self):
        for item in os.listdir(self.path):
            # self.dirContents.append(os.path.splitext(item)[0])
            self.dirContents.append(item)
    
    def renameDir(self, oldName, newName):
        os.rename(os.path.join(self.path, oldName), os.path.join(self.path, newName))

    def getFileContents(self):
        words = []
        with open (self.path, 'r') as myFile:
            index = -1
            for line in myFile:
                for word in line.split(' '):
                    index += 1 
                    if ('\n' in word):
                        self.newLineIndies.add(index)
                        word = word.rstrip('\n')
                    if (word != ""):
                        words.append(word)
        return words

    def changeFileContents(self, words):
        for x in self.newLineIndies:
            words[x] = words[x] + "\n"
        
        output = ""
        for index, word in enumerate(words):
            if (index in self.newLineIndies):
                output += word
            else:
                output += word + " "
        output = output.strip()
        
        with open (self.path, 'w+') as myFile:
            myFile.write(output)
            myFile.seek(0)

    def createNewFile(self, words):
        for x in self.newLineIndies:
            words[x] = words[x] + "\n"
        
        output = ""
        for index, word in enumerate(words):
            if (index in self.newLineIndies):
                output += word
            else:
                output += word + " "
        output = output.strip()

        tempPath, fileName = os.path.split(self.path)
        oldFileName = os.path.splitext(fileName)
        newFileName = oldFileName[0] + "-New" + oldFileName[1]
        tempPath = os.path.join(tempPath, newFileName)
        
        with open (tempPath, 'w+') as myFile:
            myFile.write(output)
            myFile.seek(0)