def total(*numbers):
    """
    *args collects each argument separately.
    Passing a list creates ONE argument: the list itself.
    """
    return sum(numbers)

def main():
    print("- total(1,2,3):", total(1, 2, 3))

    nums = [1, 2, 3]

    # ❌ WRONG: passing the whole list as a single argument
    try:
        print("- total(nums):", total(nums))
    except Exception as e:
        print("  ERROR:", e)

    # ✅ CORRECT: unpack the list into separate arguments
    print("- total(*nums):", total(*nums))

if __name__ == "__main__":
    main()
