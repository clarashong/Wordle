import os
import openpyxl
import random

# WordChooser works with the file "wordsList.xlsx" (that was prepared by WordsListGenerator) 
class WordChooser:
    def __init__(self, letters):
        # name of sheet 
        self.sheet = str(letters) + " letters"
        # name of excel file
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




