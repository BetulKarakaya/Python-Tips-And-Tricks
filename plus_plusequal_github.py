def main():
    print("\n--- INTEGER (immutable) ---")
    a = 10
    b = a

    a += 5
    print("a:", a)   # 15
    print("b:", b)   # 10 (unchanged)

    print("\n--- LIST (mutable) with += ---")
    list_a = [1, 2]
    list_b = list_a

    list_a += [3]
    print("list_a:", list_a)  # [1, 2, 3]
    print("list_b:", list_b)  # [1, 2, 3] ----- !!!! same object

    print("\n--- LIST (mutable) with + ---")
    list_c = [1, 2]
    list_d = list_c

    list_c = list_c + [3]
    print("list_c:", list_c)  # [1, 2, 3]
    print("list_d:", list_d)  # [1, 2] ------ !!!! unchanged


if __name__ == "__main__":
    main()
