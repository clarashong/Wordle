import tkinter as tk 
import tkinter.ttk as ttk
from GameText import GameText
from GameBoard import GameBoard
from GameSystem import GameSystem
from Input import Input
from WordChooser import WordChooser as wc 

class App(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.minsize(500,600)

        self.letters = 5 
        self.max = 5
        self.startMenu = self.genStartMenu()
        self.startMenu.pack()

        self.mainloop()

    def genStartMenu(self):
        frame = ttk.Frame(master=self)

        title = ttk.Label(master=frame, 
                          text="Wordle", 
                          font="Helvetica 40 bold")
        title.pack(pady=5)

        caption1 = "How many letters?"
        cap1 = ttk.Label(master=frame, 
                         text=caption1, 
                         font="Helvetica 16")
        cap1.pack()

        # tracking the scale value
        v = tk.IntVar()
        scale = tk.Scale(master=frame, 
                         variable=v, 
                         from_=3, to=8, 
                         orient="horizontal")  
        scale.pack(pady=3)

        # start buttton 
        button = ttk.Button(
            master=frame,
            text="READY", 
            command=lambda:self.startGame(v.get()))
        button.pack(pady=5)

        return frame
    
    # StartGame(self, num) starts the game with a solution with num letters
    # App, Int -> None
    def startGame(self, num):
        self.letters = num 
        self.max = num 

        self.startMenu.destroy()

        title = ttk.Label(text="Wordle", font="Helvetica 24 bold")
        title.pack()
        
        wordChooser = wc(self.letters) 
        solution = wordChooser.getWord()

        self.input = Input(self, GameSystem(self,self.letters,self.max,solution))

    # destroys the current game to play again 
    def playAgain(self): 
        self.destroy() 
        App ("Wordle Clone") 

if (__name__ == "__main__"):
    App("Wordle Clone") 


