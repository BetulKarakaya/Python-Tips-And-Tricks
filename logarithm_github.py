import math
import matplotlib.pyplot as plt
import numpy as np

class Log:
    
    def __init__(self, choice, number):
        self.choice = choice
        self.number = number 
        self.custom_base = None
    
    
    def calculate_logarithm(self):
    
        if self.choice == 1:
            self.log_value = math.log(self.number)  # Natural log
            print(f"\nNatural logarithm of {self.number} (base e): {self.log_value:.4f}")
        elif self.choice == 2:
            self.log_value = math.log10(self.number)  # Base 10 log
            print(f"\nLogarithm of {self.number} (base 10): {self.log_value:.4f}")
        elif self.choice == 3:
            self.custom_base = float(input("Enter the custom base: "))
            if self.custom_base <= 0 or self.custom_base == 1:
                print("Base must be greater than 0 and not equal to 1.")
                return
            self.log_value = math.log(self.number, self.custom_base)
            print(f"\nLogarithm of {self.number} (base {self.custom_base}): {self.log_value:.4f}")
        else:
            print("Invalid choice.")
            return
        

    def visualize(self):
        # Visualization

        #The NumPy.linspace() function returns an array of evenly spaced values 
        # within the specified interval [start, stop].
        x = np.linspace(1, self.number * 2, 500)
        if self.choice == 1:
            y = np.log(x)
            title = "Natural Logarithm (base e)"
        elif self.choice == 2:
            y = np.log10(x)
            title = "Logarithm (base 10)"
        else:
            y = np.log(x) / np.log(self.custom_base)
            title = f"Logarithm (base {self.custom_base})"

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f"{title}")
        plt.axvline(x=self.number, color="red", linestyle="--", label=f"Input: {self.number}")
        plt.title(f"{title} Visualization")
        plt.xlabel("Input Value")
        plt.ylabel("Logarithm Value")
        plt.legend()
        plt.grid()
        plt.gca().set_axisbelow(True)
        plt.show()


def main():
    try:
        number = float(input("Enter a positive number: "))
        if number <= 0:
            print("Logarithm is not defined for non-positive numbers.")
            return

        print("\nChoose a logarithm base:")
        print("1. Natural Logarithm (base e)")
        print("2. Logarithm (base 10)")
        print("3. Custom Base")

        choice = int(input("Enter your choice (1, 2, or 3): "))

        log_app = Log(choice = choice, number = number)
        log_app.calculate_logarithm()
        log_app.visualize()
    
    except ValueError:
        print("Invalid input. Please enter numerical values only.")

if __name__ == "__main__":
    main()
