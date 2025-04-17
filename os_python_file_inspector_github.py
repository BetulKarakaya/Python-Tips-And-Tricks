import os
import matplotlib.pyplot as plt
from collections import defaultdict

class PythonSizeGrouper:
    def __init__(self, directory):
        if not os.path.isdir(directory):
            raise NotADirectoryError("❌ This path does not exist or is not a directory.")
        self.directory = directory
        self.size_groups = defaultdict(int)

    def group_files_by_size(self):
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(root, file)
                    size_kb = os.path.getsize(path) / 1024  # convert to KB

                    if size_kb <= 5:
                        self.size_groups["0-5KB"] += 1
                    elif size_kb <= 10:
                        self.size_groups["5-10KB"] += 1
                    elif size_kb <= 50:
                        self.size_groups["10-50KB"] += 1
                    elif size_kb <= 100:
                        self.size_groups["50-100KB"] += 1
                    else:
                        self.size_groups["100KB+"] += 1

    def display_summary(self):
        if not self.size_groups:
            print("📭 No Python files found.")
            return

        print("\nPython File Size Distribution:\n")
        for group, count in self.size_groups.items():
            print(f"📦 {group}: {count} file(s)")

    def plot_bar_chart(self):
        if not self.size_groups:
            return
        
        labels = list(self.size_groups.keys())
        counts = list(self.size_groups.values())

        plt.figure(figsize=(8, 5))
        plt.bar(labels, counts, color="skyblue", edgecolor="black")
        plt.xlabel("Size Ranges (KB)")
        plt.ylabel("Number of Files")
        plt.title("Python File Size Groups", fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

def main():
    folder = input("📁 Enter a folder path to analyze Python file sizes: ").strip()
    try:
        analyzer = PythonSizeGrouper(folder)
        analyzer.group_files_by_size()
        analyzer.display_summary()
        analyzer.plot_bar_chart()
    except Exception as e:
        print(f"⚠️ {e}")

if __name__ == "__main__":
    main()