from GameText import GameText

#GameSystem controls the board and the input

class GameSystem:
    def __init__(self, letters, max, solution, input, board, guessNum=0):
        self.game = GameText(letters, max, solution)
        self.input = input
        self.board = board
        self.guessNum = guessNum
        self.solution = solution

    def main(self):
        guess = ""
        result = []
        # look for guesses / take in input
        if (self.input.getPendingGuess() == True):
            guess = self.input.getCurrentEntry()
            if (self.game.checkValid(guess)):
                # evaluate the guess
                result = self.game.evaluate(guess, self.solution)

                # update the board
                self.board.updateDisplay(self.guessNum, guess, result)
                self.guessNum += 1

                # check if there's a win or loss
            else:
                #give off message that the answer is invalid
                pass

        pass

    def takeGuess(self):
        pass


    


