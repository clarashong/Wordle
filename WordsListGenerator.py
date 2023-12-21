from english_words import get_english_words_set
from openpyxl import Workbook 


# set of words 
web2lowerset = get_english_words_set(["web2"], True, True)

# dict is a dictionary of: {# of letters : dictionary of {first letter: total}}
dict = {}

# min and max # of letters 
# must be greater than 0
min = 3 
max = 8

# new excel workbook 
wb = Workbook()

# dictionary that keeps track of the sheet names 
sheetNames = {} 

for i in range (min, max+1):
    wb.create_sheet(str(i) + " letters")
    sheetNames.update({i: str(i) + " letters"})
    dict.update({i:{}})
    
# remove the default sheet
wb.remove(wb["Sheet"])

for w in web2lowerset:
    length = len(w)
    if (min-1<length<max+1):
        sheet = wb[sheetNames.get(length)]
        ch = w[0].upper() # first letter
        cell = ""
        if (dict[length].get(ch) is None):
            dict[length].update({ch: 1})
            cell = ch + str(1) 
        else: 
            dict[length][ch] += 1
            cell = ch + str(dict[length].get(ch))
        # add word to the spreadsheet
        sheet[cell] = w

# save the file
wb.save(filename="wordsList.xlsx")