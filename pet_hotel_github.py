import time
import random

# Parent Class - Pet
class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self.energy = 50  # Energy Level (0-100)

    def make_sound(self):
        return "Some generic pet sound 🎶"

    def feed(self, food):
        self.energy = min(self.energy + 20, 100)
        return f"🍽️ {self.name} ate {food}! Energy: {self.energy}/100"

    def groom(self):
        return f"🛁 {self.name} had a spa day! Looking fresh and clean!"

    def play(self):
        return f"🎉 {self.name} played and had a great time!"
    
    def __str__(self):
        return f"{self.name} the {self.species} ({self.age} years old) - Energy: {self.energy}/100"

# Child Class - Dog
class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof! 🐶"

    def play(self):
        if self.energy < 15:
            return f"{self.name} is too tired to play fetch. 😴"
        self.energy -= 15
        return f"{self.name} fetched the ball! 🎾 Energy: {self.energy}/100"

# Child Class - Cat
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self.color = color

    def make_sound(self):
        return "Meow! 😺"

    def play(self):
        if self.energy < 10:
            return f"{self.name} is too tired to scratch furniture. 😴"
        self.energy -= 10
        return f"{self.name} scratched the couch! 😾🛋️ Energy: {self.energy}/100"

# Pet Hotel Class
class PetHotel:
    def __init__(self):
        self.guests = []

    def check_in(self, pet):
        print(f"📢 {pet.name} has checked into the Pet Hotel!")
        self.guests.append(pet)
        time.sleep(1)

    def check_out(self, pet_name):
        for pet in self.guests:
            if pet.name.lower() == pet_name.lower():
                print(f"👋 {pet.name} has checked out. Goodbye!")
                self.guests.remove(pet)
                return
        print(f"⚠️ No pet named {pet_name} in the hotel!")

    def list_guests(self):
        if not self.guests:
            print("🏨 The Pet Hotel is currently empty.")
        else:
            print("\n🏨 Current Guests in Pet Hotel:")
            for pet in self.guests:
                print(f"  - {pet} ({pet.make_sound()})")
        print("")

    def provide_services(self, pet_name, service):
        for pet in self.guests:
            if pet.name.lower() == pet_name.lower():
                if service == "feed":
                    food = random.choice(["Chicken", "Salmon", "Beef", "Tuna"])
                    print(pet.feed(food))
                elif service == "groom":
                    print(pet.groom())
                elif service == "play":
                    print(pet.play())
                return
        print(f"⚠️ No pet named {pet_name} found in the hotel!")


def main():
    hotel = PetHotel()
    print("Welcome To Our Pet Hotel".center(100, "-"))
    while True:
        try:
            print("\n1- Display Guest List")
            print("2- Check-in Customer")
            print("3- Feed Customer")
            print("4- Groom Customer")
            print("5- Play Time With Customer")
            print("6- Check-out Customer")
            print("7- Exit")
            
            choice = input("Select an option: ")
            
            if choice == "1":
                hotel.list_guests()
            elif choice == "2":
                name = input("Enter pet's name: ")
                age = int(input("Enter pet's age: "))
                species = input("Enter pet type (dog/cat): ").strip().lower()
                if species == "dog":
                    breed = input("Enter dog breed: ")
                    pet = Dog(name, age, breed)
                elif species == "cat":
                    color = input("Enter cat color: ")
                    pet = Cat(name, age, color)
                else:
                    print("⚠️ Invalid pet type!")
                    continue
                hotel.check_in(pet)
            elif choice == "3":
                pet_name = input("Enter pet name to feed: ")
                hotel.provide_services(pet_name, "feed")
            elif choice == "4":
                pet_name = input("Enter pet name to groom: ")
                hotel.provide_services(pet_name, "groom")
            elif choice == "5":
                pet_name = input("Enter pet name to play with: ")
                hotel.provide_services(pet_name, "play")
            elif choice == "6":
                pet_name = input("Enter pet name to check-out: ")
                hotel.check_out(pet_name)
            elif choice == "7":
                print("👋 Thank you for visiting Pet Hotel! Goodbye!")
                break
            else:
                print("⚠️ Invalid option! Please select a valid choice.")
        except ValueError:
            print("⚠️ Please enter valid data!")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
