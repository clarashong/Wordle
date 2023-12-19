import tkinter as tk 
import tkinter.ttk as ttk

class GameBoard:
    
    def __init__(self, letters, max):
        self.letters = letters
        self.max = max 
        self.guesses = [] #list of words guessed 
        self.results = [] #list of colours to be presented
        self.grid_frame = tk.Frame()
        self.setup()

    def setup(self):
        self.setUpGrid()
        #self.display.mainloop()

    def setUpGrid(self):
        self.grid_frame = tk.Frame(width=1, height=1)
        #self.grid_frame.pack()
        
        for row in range (self.max):
            frame = tk.Frame(master=self.grid_frame)
            self.grid_frame.rowconfigure(index=row,weight=1)
            for col in range (self.letters):
                box = tk.Label(master=frame, height=5, width=7, text="", bg="red")
                box.grid(row=0, column=col, padx=5, pady=0)
            frame.grid(row=row, padx=0, pady=5)

    def updateGuesses(self, guess):
        self.guesses.append(guess)

    def updateDisplay(self, guessNum, guess, colours):
        self.updateGuesses(guess)
        frame = self.newGuessFrame(guess, colours)
        frame.grid(row=guessNum)
    
    def newGuessFrame(self, guess, colours):
        frame = tk.Frame(master=self.grid_frame)
        for i in range(len(guess)):
            box = tk.Label(
                master=frame, 
                height=5, 
                width=7, 
                text=guess[i], 
                bg=colours[i],
                font="Helvetica 24"
            )
            box.grid(row=0, column=i, padx=5, pady=0)
        return frame

    def getGrid(self):
        return self.grid_frame


if (__name__ == "__main__"):
    board = GameBoard(5,5)



        
            
            






