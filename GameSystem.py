from GameText import GameText
from GameBoard import GameBoard
import tkinter as tk
import tkinter.ttk as ttk

#GameSystem controls the board and the input

class GameSystem(ttk.Frame):
    def __init__(self, parent, letters, max, solution, guessNum=0):
        super().__init__(parent)
        self.game = GameText(letters, max, solution)
        self.input = input
        self.max = max
        self.guessNum = guessNum
        self.solution = solution
        self.invalid = None
        self.finished = False
        self.board = GameBoard(self, letters, max)

    def update(self, guess):
        result = []

        if (self.guessNum >= self.max-1): 
            self.finished = True

        if (not self.invalid is None):
                self.invalid.destroy()
        if (self.game.checkValid(guess)):
            result = self.game.evaluate(guess, self.solution)
            self.board.updateDisplay(self.guessNum, guess, result)
            # add a guess
            self.guessNum += 1
        else:
            self.invalid = self.genInvalidMsg()
            self.invalid.pack(pady=3)

        if (guess == self.solution):
            self.finished = True

        
            

    def genInvalidMsg(self): 
        message = tk.Message(text="Invalid Guess, try again.", 
                             font="Helvetica 12", 
                             fg="#eae9de",
                             bg="#868e8b") 
        return message


    def getGuessNum(self):
        return self.guessNum

    def getMax(self):
        return self.max

    def getBoard(self):
        return self.board
    
    def getFinished(self):
        return self.finished
    
    def getSolution(self):
        return self.solution
    

    




    


