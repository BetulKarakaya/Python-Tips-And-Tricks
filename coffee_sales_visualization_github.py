import matplotlib.pyplot as plt
import numpy as np

def visualize_coffee_sales(coffee_types, sales):

    plt.figure(figsize=(8, 6))
    plt.bar(coffee_types, sales, color='saddlebrown', alpha=0.8)

    
    plt.title("Daily Coffee Sales", fontsize=16, fontweight='bold')
    plt.xlabel("Coffee Types", fontsize=12)
    plt.ylabel("Number of Cups Sold", fontsize=12)

    plt.yticks(np.arange(0, max(sales)+ 1, 5))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.gca().set_axisbelow(True)

   
    for i, value in enumerate(sales):
        plt.text(i, value + 1, str(value), ha='center', fontsize=10)


    plt.tight_layout()
    plt.show()


def main():
    
    coffee_types = ["Espresso", "Latte", "Cappuccino", "Americano", "Mocha", "Turkish Coffee"]
    sales = [25, 40, 35, 20, 15, 45]


    print("Welcome To Our Coffee Sales Visualization Program Let's Visualize!!!".center(100))
    visualize_coffee_sales(coffee_types= coffee_types, sales= sales)
    print("Good Byee".center(100))

if __name__ == "__main__":
    main()