def main():
    user = {
        "name": "Betül",
        "age": None
    }

    print("\n--- DIRECT ACCESS (dict[key]) ---")
    try:
        print("Age:", user["age"])        # Key exists → returns None
        print("City:", user["city"])      # ❌ Key does NOT exist → KeyError
    except KeyError as e:
        print("KeyError:", e)

    print("\n--- SAFE ACCESS (dict.get) ---")
    print("Age:", user.get("age", 18))    # Key exists → None (default ignored)
    print("City:", user.get("city", "Unknown"))  # Key missing → default value

    print("\n--- IMPORTANT DETAIL ---")
    print("Before get():", user)
    user.get("country", "Turkey")         # get() does NOT create a key
    print("After get():", user)

    print("\n--- WHEN TO USE WHICH ---")
    print("- Use dict[key]  → when key MUST exist")
    print("- Use dict.get() → when key is optional or risky")


if __name__ == "__main__":
    main()
