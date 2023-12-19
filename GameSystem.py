from GameText import GameText
from Input import Input
from GameBoard import GameBoard

#GameSystem controls the board and the input

class GameSystem:
    def __init__(self, letters, max, solution, input, board, guessNum=0):
        self.game = GameText(letters, max, solution)
        self.input = input
        self.board = board
        self.max = max
        self.guessNum = guessNum
        self.solution = solution

    def main(self):
        
        while (self.guessNum < self.max):
            guess = ""
            result = []
            print("game is functioning")
            # look for guesses / take in input
            if (self.input.getPendingGuess() == True):
                print ("pending guess is true")
                guess = self.input.getCurrentEntry()
                if (self.game.checkValid(guess)):
                    # evaluate the guess
                    print ("evaluating" + guess)
                    result = self.game.evaluate(guess, self.solution)

                    # update the board
                    print("updating display")
                    self.board.updateDisplay(self.guessNum, guess, result)
                    # add a guess
                    self.guessNum += 1

                    # check if there's a win or loss
                    if (self.game.getFinished == True):
                        #display some sort of ending screen
                        pass
                else:
                    #give off message that the answer is invalid
                    pass
                self.input.setPendingGuess(False)
        pass

    def takeGuess(self):
        pass

    def getBoard(self):
        return self.board
    
    def getInput(self):
        return self.input




    


