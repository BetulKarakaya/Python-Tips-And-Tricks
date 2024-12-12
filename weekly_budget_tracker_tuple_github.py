# Weekly Budget Tracker
# This program uses tuples to represent weekly expenses for different categories
# and calculates whether the total expenses stay within a predefined budget.
def main():
    # Define a tuple for the weekly budget per category (in dollars)
    # Each element represents (category, allocated_budget)
    weekly_budget = (
        ("Groceries", 150),
        ("Transportation", 50),
        ("Entertainment", 80),
        ("Utilities", 120),
        ("Miscellaneous", 60)
    )

    # Define another tuple for the actual expenses per category
    weekly_expenses = (
        ("Groceries", 140),
        ("Transportation", 55),
        ("Entertainment", 90),
        ("Utilities", 115),
        ("Miscellaneous", 70)
    )

    compare_expenses_and_budget(weekly_budget = weekly_budget, weekly_expenses = weekly_expenses)
    final_summary_budget_total(weekly_budget = weekly_budget, weekly_expenses = weekly_expenses)

def final_summary_budget_total(weekly_budget,weekly_expenses):
    # Calculate total budget and total expenses
    # Extract second element of each tuple using a tuple unpacking technique
    total_budget = sum(budget for _, budget in weekly_budget)
    total_expenses = sum(expense for _, expense in weekly_expenses)
    
    # Display Summary
    print("Total Allocated Budget:", f"${total_budget}")
    print("Total Expenses:", f"${total_expenses}")
    if total_expenses > total_budget:
        print("Warning: You exceeded your total budget by $", total_expenses - total_budget)
    elif total_expenses == total_budget:
        print("Good job! You spent exactly within your budget.")
    else:
        print("Great! You stayed under your budget by $", total_budget - total_expenses)

def compare_expenses_and_budget(weekly_budget,weekly_expenses):
    
    # Compare and output results
    print("Weekly Budget Summary")
    print("----------------------")
    for category, budget in weekly_budget:
        # Find the corresponding expense for the same category
        # Find the actual expense for the given category using next() 
        # and a generator expression. This efficiently retrieves the first 
        # matching expense from the list of tuples.
        expense = next((amount for cat, amount in weekly_expenses if cat == category), 0)
        status = "Under Budget" if expense <= budget else "Over Budget"
        print(f"Category: {category}\n  Allocated: ${budget}\n  Spent: ${expense}\n  Status: {status}\n")

if __name__  == "__main__":
    main()