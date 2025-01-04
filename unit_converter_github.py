def unit_converter(choice,distance): # choice -> user choise input
    """
    A simple unit converter for distances (kilometers, miles, meters, feet).
    """

    # Dictionary of conversion rates
    conversion_rates = {
        "kilometers_to_miles": 0.621371,
        "kilometers_to_meters": 1000,
        "kilometers_to_feet": 3280.84,
        "miles_to_kilometers": 1.60934,
        "meters_to_kilometers": 0.001,
        "feet_to_kilometers": 0.0003048
    }
    # Perform conversion based on user's choice
    conversion_map = {
        "1": ("kilometers_to_miles", "miles"),
        "2": ("kilometers_to_meters", "meters"),
        "3": ("kilometers_to_feet", "feet"),
        "4": ("miles_to_kilometers", "kilometers"),
        "5": ("meters_to_kilometers", "kilometers"),
        "6": ("feet_to_kilometers", "kilometers"),
    }

    if choice in conversion_map:
        conversion_type, unit = conversion_map[choice]
        converted_distance = distance * conversion_rates[conversion_type]
        print(f"\n✨ {distance} converted to {unit} is: {converted_distance:.2f} {unit}")
    else:
        print("❌ Invalid choice. Please try again!")

def main(): 
    
    print("🌍 Welcome to the Unit Converter! 🌍")
    print("Convert distances between kilometers, miles, meters, and feet.")
    
    try:
        distance = float(input("Enter the distance: "))
    except:
        raise ValueError("Distance value isn't numerical")
    
    print("\nChoose the conversion type:")
    print("1. Kilometers to Miles")
    print("2. Kilometers to Meters")
    print("3. Kilometers to Feet")
    print("4. Miles to Kilometers")
    print("5. Meters to Kilometers")
    print("6. Feet to Kilometers")
    
    try:
        choice = input("Enter your choice (1-6): ").strip()
    except:
        raise ValueError()

    unit_converter(choice= choice, distance = distance)

if __name__ == "__main__":
    main()
