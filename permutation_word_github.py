import math
from itertools import permutations

class InvalidRError(Exception):
    def __init__(self, r, word):
        super().__init__(f"{r} must be bigger than 0 and smaller than length of word {word} - {len(word)}")
        
        
""" The r-letter permutation of an n-letter word. """
class Permutation:
    def __init__(self, word, r):
        self.word = word
        self.r = r
        self.permutation_list = list(self.word)  
        self.n = len(self.permutation_list) 

    def calculate_permutation(self):
     
        self.result = math.factorial(self.n) / math.factorial(self.n - self.r)

    def print_all_permutations(self):
       
        all_perm = permutations(self.permutation_list, self.r)
        all_perm_list = list(all_perm)
        
        print(f"The List Of {self.r}-Letter Permutation Of {self.word}")
        for i, perm in enumerate(all_perm_list):
            print(f"{i+1}. Permutation -> {''.join(perm)}")  
    
    def print_result(self):
       
        print(f"The r-letter permutation of the word\nr: {self.r}, word: {self.word}\n")
        print(f"The total number of {self.r}-permutations of the word {self.word}: {self.result}")
        self.print_all_permutations()
    
    def main_app(self):
        self.calculate_permutation()
        self.print_result()

def main():
    try:
        print("A program that calculates the given r-permutation of the entered word.")
        word = input("Enter a word: ").strip().split()[0]  
        r = int(input("Enter r value (r must be bigger than 0 and smaller than length of word): "))
        
        if r <= 0 or r > len(word):  
            raise InvalidRError(r, word)
        
        app = Permutation(word=word, r=r)
        app.main_app()
    
    except Exception as e:
        print(f"Error: Something Went Wrong 🥲 \n {e}")

if __name__ == "__main__":
    main()
