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
        
        self.input = Input(self, GameSystem(self,5,5,"pound"))

        self.mainloop()

App("Wordle Clone")