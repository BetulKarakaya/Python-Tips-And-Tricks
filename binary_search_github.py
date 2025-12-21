def binary_search(sorted_numbers, target):
    """
    Binary Search using Divide & Conquer logic.
    Works ONLY on sorted lists.
    """

    left = 0
    right = len(sorted_numbers) - 1

    print(f"* Searching for: {target}")
    print(f"* List: {sorted_numbers}\n")

    while left <= right:
        mid = (left + right) // 2

        print(f"- Left index : {left}")
        print(f"- Mid index  : {mid}")
        print(f"- Right index: {right}")
        print(f"- Value: {sorted_numbers[mid]}\n")

        if sorted_numbers[mid] == target:
            print(f"✅ Found {target} at index {mid}")
            return mid

        elif sorted_numbers[mid] < target:
            print(f"- {sorted_numbers[mid]} < {target} → search RIGHT side\n")
            left = mid + 1

        else:
            print(f"- {sorted_numbers[mid]} > {target} → search LEFT side\n")
            right = mid - 1

    print(f"❌ {target} not found")
    return -1

def main():
    numbers = [2, 5, 7, 10, 14, 20, 33, 40]
    binary_search(numbers, 14)

if __name__ == "__main__":
    main()
