import tkinter as tk 
import tkinter.ttk as ttk
from GameSystem import GameSystem

class Input(ttk.Frame):
    def __init__(self, parent, gs):
        super().__init__(parent)
        self.pendingGuess = False
        self.currentEntry = ""
        self.parent = parent
        
        #game system
        self.gs = gs

        #frame with entry area and button 
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
        self.currentEntry = self.entryWord.get().lower()
        self.pendingGuess = True
        self.entry.delete(0, 'end')

        self.gs.update(self.currentEntry)
        
        if (self.gs.getFinished()):
            if (self.gs.getGuessNum() < self.gs.getMax()):
                screen = self.genWinScreen() 
                screen.pack() 
            else: 
                if (self.currentEntry == self.gs.getSolution()):
                    screen = self.genWinScreen()   
                else: 
                    screen = self.genLoseScreen() 
                screen.pack() 
            self.destroy() 
        
        
    
    def genWinScreen(self): 
        screen = tk.Frame() 
        title = ttk.Label(master=screen, 
                          text="YOU WIN!", 
                          font="Helvetica 40 bold")
        title.pack(pady=5)

        message = tk.Label(master=screen,
                            text="Congrats you got it in {} guesses!".format(self.gs.getGuessNum()),
                            font="Helvetica 12",
                            anchor="center") 
        message.pack(expand=True)

        # play again button 
        button = ttk.Button(
            master=screen,
            text="PLAY AGAIN", 
            command=self.restart)
        button.pack(pady=5)

        return screen 
        
    def genLoseScreen(self):
        screen = tk.Frame() 
        title = ttk.Label(master=screen, 
                          text="YOU LOSE!", 
                          font="Helvetica 40 bold")
        title.pack(pady=5)

        message = tk.Label(master=screen,
                            text="The correct answer was " + self.gs.getSolution().upper() +".", 
                            font="Helvetica 12")
        message.pack()

        # play again button 
        button = ttk.Button(
            master=screen,
            text="PLAY AGAIN", 
            command=self.restart)
        button.pack(pady=5)

        return screen 

    def restart(self):
        self.parent.playAgain()

        

    def getPendingGuess(self):
        return self.pendingGuess
    
    def getCurrentEntry(self):
        return self.currentEntry
    
    def setPendingGuess(self, new):
        self.pendingGuess = new
