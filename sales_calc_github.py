from itertools import accumulate
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    # Example data: Daily income and expenses in Turkish Lira
    daily_income = [100, 200, 150, 300, 250, 400, 350]
    daily_expense = [-20, -50, -30, -40, -80, -100, -50]

    # Daily net (income - expense)
    daily_net = [income + expense for income, expense in zip(daily_income, daily_expense)]
    
    # Cumulative total of net income
    cumulative_net = list(accumulate(daily_net))

    # Plot the data
    plt.figure(figsize = (10, 6))
    plt.plot(range(1, len(daily_income) + 1), daily_income, marker = "o", label = "Daily Income (₺)", color = "green")
    plt.plot(range(1, len(daily_expense) + 1), daily_expense, marker ="x", label = "Daily Expense (₺)", color ="red")
    plt.plot(range(1, len(cumulative_net) + 1), cumulative_net, marker = "s", label = "Cumulative Net (₺)", linestyle = "--", color = "blue")

    # Customize the plot
    plt.title("Daily Income, Expenses, and Cumulative Net Report", fontsize=14)
    plt.xlabel("Days", fontsize = 12)
    plt.ylabel("Amount (₺)", fontsize = 12)
    plt.xticks(range(1, len(daily_income) + 1))
    plt.axhline(0, color = "black", linestyle = "--", linewidth = 0.8)  # Add a horizontal line at 0 for reference
    plt.legend()
    plt.grid(True, linestyle = "--", alpha = 0.6)
    plt.show()
