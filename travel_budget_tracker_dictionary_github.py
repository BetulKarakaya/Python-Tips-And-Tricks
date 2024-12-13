# Travel Budget Tracker: Calculate the remaining budget for each category of a travel plan
# using dictionaries for storing the planned and actual expenses.

# Function to display budgets and expenses in a tabular format
def display_budget(planned_budget, actual_expenses):
    print("Trip Budget Overview:\n")
    print("Category         | Planned ($) | Actual ($) | Difference ($)")
    print("-----------------------------------------------------------")
    
    for category in planned_budget:
        planned = planned_budget[category]
        actual = actual_expenses.get(category, 0)  # Use get() to avoid KeyError for missing categories
        difference = planned - actual
        print(f"{category:<15} | {planned:<11} | {actual:<10} | {difference:<12}")
    
    print("\n\n")


def calculate_remaining_budget(planned_budget, actual_expenses):
    # Calculate the remaining budget for each category
    remaining_budget = {
        category: planned_budget[category] - actual_expenses.get(category, 0)
        for category in planned_budget
    }
    return remaining_budget


def display_remaning_budget(remaining_budget):
    # Display the results in a user-friendly way
    print("Travel Budget Summary:\n")
    for category, remaining in remaining_budget.items():
        if remaining > 0:
            print(f"  You stayed within budget for {category}. Remaining: ${remaining}.")
        elif remaining == 0:
            print(f"  Perfect spending on {category}. No remaining budget.")
        else:
            print(f"  Overspent on {category} by ${abs(remaining)}!")


def total_budget_difference(planned_budget, actual_expenses):
    # Calculate and display the total budget difference
    total_planned = sum(planned_budget.values())
    total_actual = sum(actual_expenses.values())
    total_difference = total_planned - total_actual
    return total_difference


def display_total_diffrenece_results(total_difference):
    
    if total_difference > 0:
        print(f"\nGreat job! You saved a total of ${total_difference} on this trip!")
    elif total_difference == 0:
        print("\nYou perfectly matched your planned budget. Excellent budgeting!")
    else:
        print(f"\nYou overspent by a total of ${abs(total_difference)}. Adjust for next time!")


def main():
    # Dictionary representing the planned budget for a trip
    planned_budget = {
        "Accommodation": 500,
        "Food": 200,
        "Transport": 150,
        "Entertainment": 100,
        "Shopping": 75,
    }

    # Dictionary representing the actual expenses made during the trip
    actual_expenses = {
        "Accommodation": 450,
        "Food": 220,
        "Transport": 180,
        "Entertainment": 90,
        "Shopping": 100,
    }
    
    display_budget(planned_budget = planned_budget, actual_expenses = actual_expenses)
    
    remaining_budget = calculate_remaining_budget(planned_budget = planned_budget, actual_expenses = actual_expenses)
    display_remaning_budget(remaining_budget = remaining_budget)
    
    total_difference = total_budget_difference(planned_budget = planned_budget, actual_expenses = actual_expenses)
    display_total_diffrenece_results(total_difference = total_difference) 


if __name__ == "__main__":
    main()