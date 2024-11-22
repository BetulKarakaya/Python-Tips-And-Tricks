import itertools
import random

def randomize_menu_selection(appetizers, main_courses, desserts):
    # Generate all possible menu combinations
    menu_combinations = list(itertools.product(appetizers, main_courses, desserts))
    #random.choice selects a random element from a non-empty sequence, 
    # such as a list or tuple.
    return random.choice(menu_combinations)

if __name__ == "__main__":
    
    # Define the menu items
    appetizers = ["Mantı", "Sarma", "Çiğ Köfte", "Soslu Patates"]
    main_courses = ["Kebab", "İçli Köfte", "Pide", "Lahmacun"]
    desserts = ["Turkish Ice Cream", "Baklava", "Künefe", "Kadayıf"]

    random_menu = randomize_menu_selection(appetizers, main_courses, desserts)

    print("Today's random menu suggestion:")
    print(f"Appetizer: {random_menu[0]}")
    print(f"Main Course: {random_menu[1]}")
    print(f"Dessert: {random_menu[2]}")
