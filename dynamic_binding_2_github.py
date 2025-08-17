class Transportation:
    def move(self):
        print("Moving from one place to another...")

class Car(Transportation):
    def move(self):
        print("Driving on the road")

class Bus(Transportation):
    def move(self):
        print("Carrying many passengers on the road")

class Airplane(Transportation):
    def move(self):
        print("Flying in the sky")

def main():
    vehicles = [Car(), Bus(), Airplane()]
    for vehicle in vehicles:
        vehicle.move()

if __name__ == "__main__":
    main()
