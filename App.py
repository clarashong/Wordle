import tkinter as tk 
import tkinter.ttk as ttk
from GameText import GameText
from GameBoard import GameBoard
from GameSystem import GameSystem
from Input import Input

class App(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.minsize(500,600)

        title = ttk.Label(text="Wordle", font="Helvetica 24 bold")
        title.pack()
        
        self.input = Input(self)

        self.mainloop()



App("Wordle Clone")


"""
def main():
    input = Input()
    board = GameBoard(5,5)
    game = GameSystem(5,5,"pound",board)
    window = tk.Tk()
    title = ttk.Label(text="Wordle", font="Helvetica 24 bold")
    title.pack()

    game.getBoard().getGrid().pack()
    input.getInterface().pack()

    while(True):
        print("window loop")
        if (input.getPendingGuess()):
            print("trying to update game")
            game.update(input.getCurrentEntry())
            input.setPendingGuess(False)
        window.mainloop()

    
def chooseWord(letters):
    pass

if (__name__ == "__main__"):
    main()

"""