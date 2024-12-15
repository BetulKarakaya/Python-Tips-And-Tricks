import time

def parking_lot(max_capacity):
    """
    A generator function to simulate a parking lot system.
    """
    parking_spots = []  # List to store currently parked cars
    print(f"Parking Lot Opened! Maximum capacity: {max_capacity} cars.\n")
    
    while True:
        # Wait for a new car to enter or leave
        action, car_number = yield parking_spots  # Yield the current parking state
        if action == "enter":
            if len(parking_spots) < max_capacity:
                parking_spots.append(car_number)
                print(f"Car {car_number} has parked. Spots left: {max_capacity - len(parking_spots)}.")
            else:
                print(f"Car {car_number} couldn't park. Lot is full!")
        elif action == "exit":
            if car_number in parking_spots:
                parking_spots.remove(car_number)
                print(f"Car {car_number} has exited. Spots left: {max_capacity - len(parking_spots)}.")
            else:
                print(f"Car {car_number} is not in the parking lot!")

if __name__ == "__main__":
    # Create a parking lot generator with a maximum capacity of 5 cars
    parking_generator = parking_lot(max_capacity=5)
    next(parking_generator)  # Prime the generator

    # Simulate cars entering and leaving
    actions = [("enter", 101), ("enter", 102), ("enter", 103), 
               ("exit", 102), ("enter", 104), ("enter", 105), 
               ("enter", 106), ("exit", 101), ("enter", 107)]
    
    for action, car_number in actions:
        parking_state = parking_generator.send((action, car_number))  # Send action to generator
        print(f"Current Parking Lot: {parking_state}\n")
        time.sleep(1)  # Simulate real-time delay
