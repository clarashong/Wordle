# Wordle clone game - December 2023

class Game:
    def __init__(self, letters, max, solution, guessNum=0):
        self.letters = letters
        self.guessNum = guessNum
        self.max = max
        self.solution = solution


    def main(self):
        solList = list(self.solution)
        while (self.guessNum < self.max):
            guess = self.takeGuess()
            result = self.evaluate(guess, solList)
            print(result)
            if (self.checkWin(result)):
                print("Congrats, you won!")
                return
        print("Too bad, you're out of guesses")
        print("The answer was " + self.solution)
        return

    # takeGuess(self) takes input as a guess, checks it, and evaluates its accuracy
    def takeGuess(self):
        guess = input("Enter a guess: ")
        while (not self.checkValid(guess)):
            guess = input("Not valid. Try again: ")
        self.guessNum += 1
        return guess

    def checkValid(self, guess):
        if (isinstance(guess, str) and guess.isalpha() and len(guess) == self.letters):
            return True
        else:
            return False
    
    # evaluate(self, guess, sol) takes in the use guess and the solution 
    # returns a len(sol) array with letters representing correctness 
    # Green - correct, Yellow - right letter wrong spot, Gray - wrong letter
    def evaluate(self, guess, sol): 
        result = []
        guess = list(guess)
        checked = set()

        #checks for all the greens first
        for i in range (0, len(sol)):
            #right letter, right space
            if (guess[i] == sol[i]):
                result.append("Green")
                checked.add(i)
            else: result.append("")

        for i in range (0, len(sol)):
            #get where that letter is located
            index = self.contains(guess[i], sol)
            if (result[i] == "") :
                #latest not checked occurence of letter
                if (index in checked and index < len(sol)-1):
                    index = self.contains(guess[i], sol[index+1::])
                
                #letter not found in solution
                if (index == False):
                    result[i] = "Gray"
                #right letter, wrong space, and now checked already
                elif(not index in checked) :
                    result[i] = "Yellow"
                    checked.add(index)
                #wrong letter, wrong space
                else:
                    result[i] = "Gray"
        return result
            
    # contains (n, lst) searches for n within lst, returns the index of lst, if found. 
    # Else returns false
    @staticmethod
    def contains(n, lst):
        for i, d in enumerate(lst):
            if (n == d):
                return i
        return False

    def getGuessNum(self):
        return self.guessNum
    
    #checkWin(result) returns true if every entry of result is Green
    @staticmethod
    def checkWin(result):
        for x in result:
            if (not x == "Green"):
                return False
        return True

def main():
    print("blah")
    game = Game(5, 5, "pound")
    game.main()

if (__name__ == "__main__"):
    main()
            




    
    


        


