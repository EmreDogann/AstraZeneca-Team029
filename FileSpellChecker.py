from spellchecker import SpellChecker
import os

class FileSpellChecker:
    def __init__(self, fileNames):
        self.fileNames = fileNames
        self.spell = SpellChecker()

    def spellCheck(self):
        
        for fileName in self.fileNames:
            # without extension
            fileNameWithoutExt = os.path.splitext(fileName)[0]
            suggestion = self.spell.correction(str(fileNameWithoutExt))
            if(fileNameWithoutExt != suggestion):
                candidates = self.spell.candidates(str(fileNameWithoutExt))
                print("Word : " + fileNameWithoutExt)
                print("    Spell Suggestion : " + suggestion)
                print("    Other Suggestion : ", candidates)



# cd ~/Downloads/GitHub/AstraZenica-Team029
# cd ~/Downloads/GitHub/testDir
# TESTING
names= []
path = r'C:\Users\Emre\Downloads\GitHub\testDir'
for item in os.listdir(path):
    if(item[0] != '.'):
        names.append(item)

checker = FileSpellChecker(names)

checker.spellCheck()