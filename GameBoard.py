import tkinter as tk 
import tkinter.ttk as ttk

class GameBoard(ttk.Frame):
    
    def __init__(self, parent, letters, max):
        super().__init__(parent)
        self.letters = letters
        self.max = max 
        self.guesses = [] #list of words guessed 
        self.results = [] #list of colours to be presented
        self.setup()


    def setup(self):
        self.setUpGrid()
        self.pack()

    def setUpGrid(self):
        for row in range (self.max):
            frame = tk.Frame(master=self)
            self.rowconfigure(index=row,weight=1)
            for col in range (self.letters):
                box = tk.Label(master=frame, height=2, width=3, text="  ", bg="#c1ccc8", font="Helvetica 28 bold")
                box.grid(row=0, column=col, padx=5, pady=0)
            frame.grid(row=row, padx=0, pady=5)

    def updateGuesses(self, guess):
        self.guesses.append(guess)

    def updateDisplay(self, guessNum, guess, colours):
        self.updateGuesses(guess)
        frame = self.newGuessFrame(guess, colours)
        frame.grid(row=guessNum)
    
    def newGuessFrame(self, guess, colours):
        frame = tk.Frame(master=self)
        for i in range(len(guess)):
            if (colours[i] == "green"):
                colours[i] = "#6AAA67"
            elif (colours[i] == "gray"):
                colours[i] = "#787C7E"
            else: 
                colours[i] = "#C9B45D" #yellow

            box = tk.Label(
                master=frame, 
                height=2, 
                width=3, 
                text=guess[i].upper(), 
                bg=colours[i],
                fg="white",
                font="Helvetica 28 bold"
            )
            box.grid(row=0, column=i, padx=5, pady=0)
        return frame

    





        
            
            






