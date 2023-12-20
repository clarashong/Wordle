import tkinter as tk 
import tkinter.ttk as ttk
from GameSystem import GameSystem

class Input(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pendingGuess = False
        self.currentEntry = ""

        self.gs = GameSystem(self,5,5,"pound")

        self.inputFrame = ttk.Frame(master=self)
        self.entry = ttk.Entry()
        self.entryWord = tk.StringVar()
        self.submit = ttk.Button()

        #setup the display
        self.setup()
    
    #setup(self) initialises the interface 
    def setup(self):
        self.columnconfigure(index=0,weight=2)
        self.columnconfigure(index=1,weight=1)
        self.entry = ttk.Entry(master=self.inputFrame, textvariable=self.entryWord)
        self.submit = ttk.Button(master=self.inputFrame, text="Submit", command=self.pressed)

        self.entry.grid(row=0, column=0, padx=2, sticky="W")
        self.submit.grid(row=0, column=1, padx=2, sticky="W")
    
        self.gs.pack()
        self.inputFrame.pack()
        self.pack()


    #pressed will return the current guess that within entry
    def pressed(self):
        self.currentEntry = self.entryWord.get()
        self.pendingGuess = True
        print ("pending guess is true")
        print (self.currentEntry)
        self.entry.delete(0, 'end')
        self.gs.update(self.currentEntry)
        return
    
    def getPendingGuess(self):
        return self.pendingGuess
    
    def getCurrentEntry(self):
        return self.currentEntry
    
    def setPendingGuess(self, new):
        print ("pending guess is now "+ new)
        self.pendingGuess = new

"""
class Input:
    def __init__(self):
        self.interface = tk.Frame()
        self.pendingGuess = False
        self.currentEntry = ""
        self.entry = ttk.Entry()
        self.entryWord = tk.StringVar()
        self.submit = ttk.Button()

        #setup the display
        self.setup()
    
    #setup(self) initialises the interface 
    def setup(self):
        self.interface.columnconfigure(index=0,weight=2)
        self.interface.columnconfigure(index=1,weight=1)
        self.entry = ttk.Entry(master=self.interface, textvariable=self.entryWord)
        self.submit = ttk.Button(master=self.interface, text="Submit", command=self.pressed)

        self.entry.grid(row=0, column=0, padx=2, sticky="W")
        self.submit.grid(row=0, column=1, padx=2, sticky="W")

    #pressed will return the current guess that within entry
    def pressed(self):
        self.currentEntry = self.entryWord.get()
        self.pendingGuess = True
        print ("pending guess is true")
        print (self.currentEntry)
        self.entry.delete(0, 'end')
        return
    
    #Accessors and modifiers 
    def getInterface(self):
        return self.interface
    
    def getPendingGuess(self):
        return self.pendingGuess
    
    def getCurrentEntry(self):
        return self.currentEntry
    
    def setPendingGuess(self, new):
        print ("pending guess is now "+ new)
        self.pendingGuess = new

        
if (__name__ == "__main__"):
    window = tk.Tk()
    input = Input()
    interface = input.getInterface()
    interface.pack()
    window.mainloop()

"""