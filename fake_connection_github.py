import time

class FakeConnection:
    def __init__(self, name: str):
        self.name = name
        print(f"Connection {self.name} established")

    def send(self, message: str):
        print(f"Sending: {message}")

    def __del__(self):
        # Called automatically when object is deleted (goes out of scope)
        print(f"Connection {self.name} closed")

def main():
    print("Program started")
    conn = FakeConnection("Server_A")
    conn.send("Hello, World!")
    time.sleep(1)
    print("Program ends, connection will be cleaned up automatically...")

if __name__ == "__main__":
    main()
