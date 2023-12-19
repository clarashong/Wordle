import tkinter as tk 
import tkinter.ttk as ttk

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
        self.pendingGuess = new

        
if (__name__ == "__main__"):
    window = tk.Tk()
    input = Input()
    interface = input.getInterface()
    interface.pack()
    window.mainloop()