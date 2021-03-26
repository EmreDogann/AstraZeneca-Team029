from spellchecker import SpellChecker
import os

'''
https://docs.python.org/3.6/library/string.html#string.printable
string.printable

    String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.
'''
from string import printable
SPECIAL_CHARACTERS = "!@#$%^&*()-+?_=,<>/"
ALPHABET = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'


class FileSpellChecker:
    def __init__(self, fileNames):
        self.fileNames = fileNames
        self.spell = SpellChecker()

    def spellCheck(self):
        # [(original, extension, [replacements, ..., ...]), ..., ...]
        wordsWithSuggestions = []
        for fileName in self.fileNames:
            
            # without extension
            fileNameWithoutExt = os.path.splitext(fileName)[0]
            extension = os.path.splitext(fileName)[1] 
            print("NAME: " + str(fileName))
            wordArray = self.cleanUp(fileNameWithoutExt)

            # if it is only one word
            if(len(wordArray) == 1):
                suggestion = self.spell.correction(str(fileNameWithoutExt))
                if(fileNameWithoutExt != suggestion):
                    candidates = self.spell.candidates(str(fileNameWithoutExt))
                    # print("Word : " + fileNameWithoutExt)
                    # print("    Spell Suggestion : " + suggestion)
                    # print("    Other Suggestion : ", candidates)
                    # print()
                    wordsWithSuggestions.append(self.getTupleReady(fileNameWithoutExt, extension, suggestion, candidates))

            # if it is words with special characters
            else:
                suggestion = ''
                candidates = []
                for word in wordArray:
                    suggestion += self.spell.correction(str(word))

                # Currently only giving one solution for file names with special characters. Improvement could be implemented here
                wordsWithSuggestions.append(self.getTupleReady(fileNameWithoutExt, extension, suggestion, candidates)) 
                # print("    Spell Suggestion : " + suggestion)

        return wordsWithSuggestions

    def getTupleReady(self, nameWithoutExt, extension, suggestion, candidates):
        suggestions = [suggestion]
        
        # remove the suggestion from candidates if duplicate
        # try and except avoids needing to loop through
        try:
            candidates.remove(suggestion)
        except ValueError:
            #do nothing
            pass
        
        # limits the number of candidates
        cap = 2
        count = 0
        for c in candidates:
            if(count == cap):
                break
            suggestions.append(c)
            count += 1
        return (nameWithoutExt, extension, suggestions)

    def cleanUp(self, word):
        splitWord = ['']
        splitWordIndex = 0
        isAlpha = True
        # word = 'broke)asda_wkdla-asd'
        for c in word:
            if (c in ALPHABET) and (not isAlpha):
                isAlpha = True
                splitWordIndex += 1
                splitWord.append('')
            elif (c in SPECIAL_CHARACTERS) and (isAlpha):
                isAlpha = False
                splitWordIndex += 1
                splitWord.append('')
            splitWord[splitWordIndex] += c

        return splitWord

    def restoreWord():
        pass


# cd ~/Downloads/GitHub/AstraZenica-Team029
# cd ~/Downloads/GitHub/testDir
# TESTING
names = []
path = './testDir'
for item in os.listdir(path):
    if(item[0] != '.'):
        names.append(item)

checker = FileSpellChecker(names)

for item in checker.spellCheck():
    print(item)
    print()

# #
# splitWord = ['']
# splitWordIndex = 0
# isAlpha = true
# word = 'broke)asda_wkdla-asd'
# for c in word:
#     if c in SPECIAL_CHARACTERS:
#         splitWordIndex += 1;
#         splitWord.append('')
#     splitWord[splitWordIndex] += c


# print(splitWord)


# splitWord = ['']
# splitWordIndex = 0
# isAlpha = True
# word = 'broke)asda_wkdla-asd'
# for c in word:
#     if (c in ALPHABET) and (not isAlpha):
#         isAlpha = True
#         splitWordIndex += 1
#         splitWord.append('')
#     elif (c in SPECIAL_CHARACTERS) and (isAlpha):
#         isAlpha = False
#         splitWordIndex += 1
#         splitWord.append('')
#     splitWord[splitWordIndex] += c