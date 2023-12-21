import os
import openpyxl
import random

class WordChooser:
    def __init__(self, letters):
        self.sheet = str(letters) + " letters"
        self.wb = openpyxl.load_workbook("wordsList.xlsx")
        self.word = self.genWord()

    def genWord(self): 
        randomLetter = chr(random.randint(ord('A'), ord('Z')))
        sheet = self.wb[self.sheet]
        word = None
        while (word is None):
            row = random.randint(1, len(sheet[randomLetter]))
            word = sheet[randomLetter + str(row)].value
        return word
    
    def getWord(self): 
        return self.word

WordChooser(5)
WordChooser(3)



