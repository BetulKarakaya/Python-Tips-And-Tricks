from pathlib import Path

def organize_files(folder):
    """
    Organizes files in the downloads folder into categorized subfolders.
    """
    # Define categories and corresponding file extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Music": [".mp3", ".wav"],
        "Archives": [".zip", ".rar", ".tar"],
        "Python Codes": [".py", ".ipynb"] # 😇
    }
    
    # Create a Path object for the given folder
    file_path = Path(folder)

    # Iterate through all files in the given folder
    for file in file_path.iterdir():
        if file.is_file():  # Check if it's a file (not a directory)
            # Match the file extension with a category
            for category, extensions in categories.items():
                if file.suffix.lower() in extensions:
                    # Create a subfolder for the category if it doesn't exist
                    category_folder = file_path / category
                    category_folder.mkdir(exist_ok=True)
                    
                    # Move the file to the categorized folder
                    file.rename(category_folder / file.name)
                    print(f"Moved: {file.name} -> {category_folder}")
                    break  # Stop checking other categories

if __name__ == "__main__":
    # Replace with the path to your any folder (you can use test folder or any folder you never organized since ice age and Sid 🦥🥶🥶🥶)
    folder_path = "C:\\your path, dont forget use \\ instead of /"
    organize_files(folder_path)
