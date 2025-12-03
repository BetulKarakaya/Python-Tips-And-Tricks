import copy

def main():
    print("\n--- WRONG WAY (shared references) ---")
    wrong_matrix = [[0] * 3] * 3   # Looks correct but all rows share the same inner list
    wrong_matrix[0][1] = 99        # Only one edit, but all rows will change!

    for row in wrong_matrix:
        print(" ", row)

    print("\n--- CORRECT WAY (independent rows) ---")
    base_row = [0] * 3
    correct_matrix =([copy.deepcopy(base_row) for _ in range(3)])  # Every row is a separate list
    correct_matrix[0][1] = 99

    for row in correct_matrix:
        print(" ", row)

if __name__ == "__main__":
    main()
