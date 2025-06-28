from contextlib import contextmanager
import time

class Device:
    def __init__(self):
        self.mode = "online"

    def set_mode(self, new_mode):
        print(f"- Switching to {new_mode.upper()} mode...")
        self.mode = new_mode
        time.sleep(1)  # simulate some delay
        print(f"- Mode is now: {self.mode.upper()}")

@contextmanager
def airplane_mode(device):
    original_mode = device.mode
    try:
        device.set_mode("offline") 
        yield
    finally:
        device.set_mode(original_mode) 

def main():
    phone = Device()

    print("* Start mode:", phone.mode.upper())

    with airplane_mode(phone):
        print("# Data processinng in Offline mode...")
        time.sleep(2)

    print("* Final mode:", phone.mode.upper())

if __name__ == "__main__":
    main()