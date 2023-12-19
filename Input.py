import tkinter as tk 
import tkinter.ttk as ttk

class Input:
    def __init__(self):
        self.interface = tk.Frame()
        self.setup()
        self.pendingGuess = False
        self.currentEntry = ""
        self.entry = tk.Entry()
        self.submit = tk.Button()
    
    def setup(self):
        self.interface.columnconfigure(index=0,weight=2)
        self.interface.columnconfigure(index=1,weight=1)

        self.entry = tk.Entry(master=self.interface)
        self.submit = tk.Button(master=self.interface, text="Submit", command=self.pressed)

        self.entry.grid(row=0, column=0, padx=2, sticky="W")
        self.submit.grid(row=0, column=1, padx=2, sticky="W")

    #pressed will return the current guess that within entry
    def pressed(self):
        self.pendingGuess = True
        self.currentEntry = self.entry.get()
        print (self.currentEntry)
        print("running")
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