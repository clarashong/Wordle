import tkinter as tk 
import tkinter.ttk as ttk
from GameText import GameText
from GameBoard import GameBoard
from Input import Input

def main():
    input = Input()
    board = GameBoard(5,5)
    game = GameText(5,5,"pound", input, board)
    window = tk.Tk()
    title = ttk.Label(text="Wordle")
    title.pack()

    gameGrid = board.getGrid()
    gameGrid.pack()
    
    submitSpace = input.getInterface()
    submitSpace.pack()

    window.mainloop()

def chooseWord(letters):
    pass

if (__name__ == "__main__"):
    main()