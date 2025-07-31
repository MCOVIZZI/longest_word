
import string
import random

class Game:
    def __init__(self):
        self.grid = []

        for _ in range(30):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            print("Look for " + letter)
            print(letters)
            if letter in letters:
                letters.remove(letter)
            else:
                print("Not possible")
                return False
            return True
