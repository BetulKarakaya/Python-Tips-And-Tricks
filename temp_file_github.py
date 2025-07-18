import tempfile

def write_temp_file():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
        temp.write("This is a temporary file.\nUsed for testing or short-term data storage.")
        temp.seek(0)
        print("File content:\n", temp.read())
        print("File path:", temp.name)

def main():
    write_temp_file()

if __name__ == "__main__":
    main()