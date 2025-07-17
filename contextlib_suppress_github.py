import os
from contextlib import suppress

class FileHandler:

    def __init__(self, file_path = "example.txt"):
        self.file_path = file_path

    def create_file(self,message = ""):
        with open(self.file_path, "w") as f:
            f.write(message)

    def read_file(self):
        with open(self.file_path, "r") as f:
            print(f.read())
    
    def add_message_to_file(self,message):
        with open(self.file_path, "a") as f:
            f.write(message)
    
    def remove_file(self):
        with suppress(FileNotFoundError):
            os.remove(self.file_path)
            print(f"File at {self.file_path} has been removed")
        

def main():
    file_handler = FileHandler("example.txt")
    file_handler.create_file()
    file_handler.add_message_to_file("Hello World\nThis is a test")
    file_handler.read_file()
    file_handler.remove_file()
    file_handler.remove_file()

if __name__ == "__main__":
    main()