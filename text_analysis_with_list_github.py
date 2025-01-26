import string
import matplotlib.pyplot as plt
import os
import numpy as np

class TextAnalysis:
    def __init__(self):
        """
        Initialize the TextAnalysis class with required attributes.
        """
        self.menu_choice = 0
        self.user_input = ""  # Holds the input text to be analyzed
        self.search_words = []  # List of words to search in the text
        self.punctuation_translator = str.maketrans('', '', string.punctuation)  # Translator to remove punctuation
        self.result = []  # List to store the result of word count analysis

    def text_analyze(self):
        """
        Analyze the text for occurrences of the specified search words.
        """
        # Clean and normalize the input text
        self.raw_text = " ".join(self.user_input.lower().split())
        self.cleaned_text = self.raw_text.translate(self.punctuation_translator)

        # Reset results before analyzing
        self.result.clear()

        # Perform word count analysis
        if self.search_words and self.cleaned_text:
            for word in self.search_words:
                count = self.cleaned_text.split().count(word)
                self.result.append({"SearchWord": word, "Count": count})

        # Visualize the results
        self.visualize()

    def visualize(self):
        """
        Visualize the word count analysis using a bar plot.
        """
        if not self.result:
            print("No data to visualize.")
            return

        # Extract words and their counts
        search_words = [data["SearchWord"] for data in self.result]
        word_counts = [data["Count"] for data in self.result]

        # Plot the bar chart
        plt.figure(figsize=(12, 5))
        plt.bar(search_words, word_counts, color="skyblue")
        plt.xlabel("Search Words")
        plt.ylabel("Counts")
        plt.title("Choosen Word Count Analysis")
        plt.grid()
        plt.gca().set_axisbelow(True)
        plt.show()

    def menu(self, choice):
        """
        Perform actions based on the menu choice provided by the user.
        """
        self.menu_choice = choice

        if self.menu_choice == 1:
            try:
                self.user_input += " " + input("Please Enter The Text: ").strip()
            except Exception as e:
                print(f"Error: {e}")

        elif self.menu_choice == 2:
            print("Current Text to Analyze:")
            print(self.user_input)

        elif self.menu_choice == 3:
            try:
                word = input("Please Enter The Word To Search: ").strip().lower()
                self.search_words.append(word)
            except Exception as e:
                print(f"Error: {e}")

        elif self.menu_choice == 4:
            print("Current Search Words:")
            print(", ".join(self.search_words))

        elif self.menu_choice == 5:
            self.user_input = ""
            print("All text cleared.")

        elif self.menu_choice == 6:
            self.search_words.clear()
            print("All search words cleared.")

        elif self.menu_choice == 7:
            if not self.user_input:
                print("No text to analyze. Please add text first.")
            elif not self.search_words:
                print("No search words added. Please add search words first.")
            else:
                self.text_analyze()

        elif self.menu_choice == 8:
            print("Exiting the program. Goodbye!")
            os._exit(0)

        else:
            print("Invalid menu choice.")


def main():
    """
    Main function to run the Text Analysis program.
    """
    condition = True
    text_analyzer = TextAnalysis()
    print("Welcome To Text Analyzer".center(100, "-"))

    while condition:
        # Display the menu
        print("1. Enter or Add Text to Analyze")
        print("2. View the Text to Analyze")
        print("3. Enter Search Word")
        print("4. View Search Words")
        print("5. Delete All Text to Analyze")
        print("6. Delete All Search Words")
        print("7. Start Analyze Process")
        print("8. Quit")

        try:
            # Get user menu choice
            choice = int(input("Please select an option: "))
            if choice <= 0 or choice > 8:
                print("Invalid menu choice. Please choose a valid option.")
            else:
                text_analyzer.menu(choice)

        except ValueError:
            print("Please enter a numerical value.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
