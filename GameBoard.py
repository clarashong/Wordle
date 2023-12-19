from Game import Game
import tkinter as tk 
import tkinter.ttk as ttk

class GameBoard:
    
    def __init__(self, letters, max):
        self.letters = letters
        self.max = max 
        self.guesses = [] #list of words guessed 
        self.results = []
        #guesses is a list of frames that will each contain a word(guess)
        self.guesses = []
        self.display = tk.Tk()
        self.display.geometry("500x700")
        self.setup()

    def setup(self):
        self.setUpGrid()
        self.display.mainloop()

    def setUpGrid(self):
        grid_frame = tk.Frame(master=self.display)
        grid_frame.pack(expand=True)
        for row in range (self.max):
            frame = tk.Frame(master=grid_frame)
            for col in range (self.letters):
                box = tk.Label(master=frame, height=5, width=7, text="", bg="red")
                box.grid(row=0, column=col, padx=5, pady=0)
            frame.grid(row=row, column=0, padx=0, pady=5)

        
            
            


if (__name__ == "__main__"):
    board = GameBoard(5,5)



        
            
            






