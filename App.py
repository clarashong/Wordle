import tkinter as tk 
import tkinter.ttk as ttk
from GameText import GameText
from GameBoard import GameBoard
from GameSystem import GameSystem
from Input import Input

def main():
    input = Input()
    board = GameBoard(5,5)
    game = GameSystem(5,5,"pound", input, board)
    window = tk.Tk()
    title = ttk.Label(text="Wordle", font="Helvetica 24 bold")
    title.pack()

    game.getBoard().getGrid().pack()
    game.getInput().getInterface().pack()
    
    window.mainloop()



    
def chooseWord(letters):
    pass

if (__name__ == "__main__"):
    main()