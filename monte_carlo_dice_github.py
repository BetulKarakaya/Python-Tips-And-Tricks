import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Dice:
    def __init__(self,num_rolls):
        self.num_rolls = num_rolls
        

    def monte_carlo_dice(self):
        self.rolls = np.random.randint(1, 7, size= self.num_rolls)  # Rolling the dice (between 1 and 6)
        self.count_six = np.sum(self.rolls == 6)  # Counting how many times 6 appeared
        self.probability = self.count_six / self.num_rolls  # Probability of rolling a 6
        return self.count_six, self.probability, self.rolls


    def display_result(self):
        print(f"Out of 100,000 rolls, the number of times 6 appeared: {self.count_six}")
        print(f"Probability of rolling a 6: {self.probability:.4f}")

    
    def visualization(self):
        df = pd.DataFrame(np.array(self.rolls))
        df = df.value_counts().reset_index().rename(columns={0: "DiceSide", "count":"Count"}).sort_values(by = ["DiceSide"], ignore_index= True)
        plt.figure(figsize=(10, 6))
        plt.bar(df["DiceSide"], df["Count"], color = "#390d6e")
        
        plt.suptitle( f"Probability of Rolling a 6 on a Die {self.probability} out of {self.num_rolls} rolls. ", color = "#272529", fontsize = 14)
        
        plt.title("Monte Carlo Dice Simulation", fontsize=16, color = "#272529", weight = "bold")
        plt.xticks([1, 2, 3, 4, 5, 6])
        plt.yticks(np.arange(0,max(df["Count"]+1000),1000))
        
        plt.grid()
        plt.gca().set_axisbelow(True)
        plt.show()
    
    
    def run(self):
        self.monte_carlo_dice()
        self.display_result()
        self.visualization()


def main():
    num_rolls = 100000
    app = Dice(num_rolls)
    app.run()


if __name__ == "__main__":
    main()