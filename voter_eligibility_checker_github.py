def check_voter_eligibility(ages):
    """
    Checks if everyone in a group is eligible to vote
    using all() and any().
    """
    print("🗳️ Voter Eligibility Checker 🗳️")

    # Check if all members are eligible
    # all(): Returns True if all elements in the iterable are True.
    # If at least one element is False, it returns False.
    # Example: Checking if all numbers in a list are non-negative.

    if all(age >= 18 for age in ages):
        print("✅ Everyone in the group is eligible to vote!")
    else:
        print("❌ Not everyone is eligible to vote.")
    
    # Check if at least one person is eligible
    # any(): Returns True if at least one element in the iterable is True.
    # If all elements are False, it returns False.
    # Example: Checking if any number in a list is positive.

    if any(age >= 18 for age in ages):
        print("👍 At least one person is eligible to vote.")
    else:
        print("👎 No one is eligible to vote.")

def main():
     # Test the function with different age groups
    group_ages = [16, 21, 18, 17]
    check_voter_eligibility(group_ages)


if __name__ == "__main__":
   main()