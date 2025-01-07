# Disclaimer:

The code provided here demonstrates the usage of the exec() function in Python for educational purposes only. By providing this code, no responsibility or liability is assumed for any consequences arising from its use. The user is solely responsible for understanding the risks associated with executing dynamic code and should exercise caution when running code provided by others.

# Python-Tips-And-Tricks

## Summary
"Python Tips and Tricks" is a curated guide offering practical, effective tips for enhancing your Python skills. Each topic includes concise code examples, outputs, and explanations for easy comprehension. Where relevant, links to external resources and official documentation are provided, allowing you to dive deeper. While the content is designed to be accessible, familiarity with basic Python concepts will enhance your experience and enable you to make the most of these tips.

| Topics                                      | Description                                                                              | Links           | Level         |
|---------------------------------------------|------------------------------------------------------------------------------------------|-----------------|---------------|
| `Lambda`                                    | Anonymous functions used for short expressions                                           | [Lambda](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/lambda_github.py)       | All Levels    |
| `String Functions - strip()`                | Removes whitespace from the start and end of a string                                    | [Remove Space Character](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/strip_func_github.py)      | All Levels    |
| `String Functions - isalpha() / isdigit() / isalnum()` | Checks for alphabetic, digit, or alphanumeric characters                          | [String Checks](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/isalpha_isdigit_github.py)       | All Levels    |
| `String Functions - capitalize() / upper() / lower() / title()` | Modifies text capitalization                                                    | [String Case Manipulation](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/string%20_case%20_manipulation_github.py)       | All Levels    |
| `String Functions - count()`                | Counts occurrences of a substring in a string                                            | [Count Of Substring](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/count_github.py)       | All Levels    |
| `String Functions - startswith() / endswith()` | Checks if a string starts or ends with a specific substring                        | [String Boundary Check](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/string_boundary_check_github.py)       | All Levels    |
| `String Functions - replace()`              | Replaces parts of a string with a specified substring                                    | [Replace](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/replace_github.py )       | All Levels    |
| `String Functions - find() / index()`       | Finds the position of a substring; raises an error if not found (`index()`)              | [Substring Locator](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/substring_locator_gihub.py)       | All Levels    |
| `String Functions - center() / ljust() / rjust()`       | The center(), ljust(), and rjust() methods align a string within a specified width, filling the extra space with a chosen character, either centering, left-aligning, or right-aligning the string.              | [Text Alignment](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/text_alignment_github.py)       | All Levels    |
| `String Functions - format_map()`       | The format_map() function replaces placeholders in a string with values from a dictionary, allowing for flexible, key-based string formatting without requiring individual variable assignments.             | [String Formatting](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/format_map_github.py)       | All Levels    |
| `String Functions - partition() / lpartition() / rpartition()`       | This example demonstrates how to use partition(), rpartition(), and the concept of lpartition() to split a string into sections based on the first or last occurrence of a separator, allowing for targeted string manipulation.             | [String Partition](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/partition_github.py)       | All Levels    |
| `For Loop`                                  | The for...else construct in Python allows you to pair a loop with an else block that executes only if the loop completes without hitting a break statement. This pattern can make code more readable by clearly distinguishing cases where a condition wasn't met during iteration. Here’s how it works: the else block runs if the loop completes all iterations without interruption; if a break is encountered, the else block is skipped. This is especially useful for search tasks, where break exits the loop if a match is found, and else handles the "no match found" case.                        | [for...else Loop](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/for_else_loop_github.py)       | Beginner      |
| `Modulo (%) Operator`                                  |  This program uses the modulo % operator to determine divisibility, replacing numbers divisible by 3 with "Fizz," by 5 with "Buzz," and by both with "FizzBuzz," creating a simple yet iconic game for learning conditional logic.             | [FizzBuzz](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/modulo_operator_github.py)       | Beginner      |
| `Reversing Lists And Strings`               | Techniques for reversing the order of elements in lists and strings                      | [Reversing Lists](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/slicing_list_github.py)       | Beginner      |
| `List Slicing`               | This code demonstrates a simple yet useful trick for named list slicing in Python. By defining key parts of a day (morning, afternoon, evening) and associating them with specific slices of a list, the code allows for dynamic access to subsets of a list based on a user-defined key. It is an example of how to combine dictionaries and list slicing to create intuitive and readable code.                     | [Daily Tasks](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/list_slicing_github.py)       | Beginner      |
| `Difference of sort() and sorted()`         | Explains in-place vs. out-of-place sorting in Python                                     | [sort() vs sorted()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/difference_of%20_sort_and_sorted_github.py)       | Beginner      |
| `Useful Function - randint()`                | This program simulates the roll of a dice using Python's **random.randint** function, which generates a random integer between 1 and 6. Each time the code runs, it mimics rolling a standard six-sided dice, making it perfect for games or random number generation scenarios.                                               | [Dice Roller](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/dice_roller_github.py)       | Beginner      |
| `Useful Function - sorted()`                | Returns a new sorted list from an iterable                                               | [sorted()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/sorted_function_github.py)       | Beginner      |
| `Useful Function - insort from bisect library` | Inserts elements into a list in sorted order                                       | [Insort](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/sort_with_bisect_github.py)       | Beginner      |
| `Useful Function - enumerate()`             | Adds a counter to an iterable for use in loops                                           | [enumerate()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/enumerate_github.py)       | Beginner      |
| `Useful Functions - enumerate() sum()`             |This ATM Simulator replicates real-life banking activities like checking balance, depositing money, withdrawing money, and viewing transaction history. It uses built-in functions like input() for user interaction, enumerate() to display transaction history, and sum() to update balances dynamically. It's interactive, practical, and fun! 🏦💵                                      | [enumerate()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/atm_simulation_beginner_github.py)       | Beginner      |
| `Useful Function - join()`                  | Joins elements of an iterable into a single string, separated by a specified delimiter   | [join()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/join_func_github.py)       | Beginner      |
| `Useful Function - set()`                   | Creates a collection of unique items from an iterable                                    | [set()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/set_func_github.py)       | Beginner      |
| `Useful Function - set() isalpha() sorted()`                   | This script analyzes the frequency of letters in a given text and displays the results as a simple ASCII bar graph.It first filters out non-alphabetic characters and normalizes the text to lowercase. Then, it calculates the frequency of each letter using a dictionary and visualizes the counts using  █ characters. This makes it both functional and visually engaging for quick analysis.                               | [ASCII Frequency Analysis](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/ascii_letter_frequency_github.py)       | Beginner      |
| `Useful Function - frozenset()`             | Creates an immutable set                                                                 | [frozenset()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/frozenset_github.py)       | Beginner      |
| `Useful Function - zip()`                   | Combines multiple iterables element-wise                                                 | [zip()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/zip_func_github.py)       | Beginner      |
| `Useful Function - zip() and zip(*)`                   | This code demonstrates the use of Python's zip() function to pair elements from two lists into a single iterable. The inventory is displayed as a clean table, and the bonus section showcases how to reverse the process with zip(*zip(...)). This is a simple yet powerful trick for organizing and working with paired data.                                             | [zip() and zip(*)](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/zip_func2_github.py)       | Beginner      |
| `Useful Function - bin()`                   | Converts an integer to a binary string                                                   | [bin()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/bin_func_github.py)       | Beginner      |
| `Useful Function - min()`                   | Returns the smallest item in an iterable                                                 | [min()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/min_func_github.py)       | Beginner      |
| `Useful Function - filter()`                | Filters elements in an iterable based on a condition                                     | [filter()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/filter_github.py)       | Beginner      |
| ` filter() and stirng manipulation`                | This code checks whether a given string is a palindrome. It normalizes the input by removing non-alphanumeric characters and converting it to lowercase, then compares the processed string with its reverse to determine if they are identical.                                  | [Palindrome Checker](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/palindrome_checker_github.py)       | Beginner      |
| ` filter() map() and sum()`                | This code takes a list of numbers, filters out the even ones using filter() and a lambda function, and calculates their total using sum(). It’s a concise and powerful example of combining built-in Python functions for clean and efficient code!                               | [Sum Of Even Numbers](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/sum_github.py)       | Beginner      |
|`Useful Function - abs()`                | This code calculates the Manhattan distance between two 2D points by summing up the absolute differences of their x and y coordinates, showcasing a practical application of the abs() function.                                     | [abs()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/absolute_distance_calculator_github.py)       | Beginner      |
|`Useful Function - all() and any()`                | This program uses **all()** to check if everyone in a group meets a condition (e.g., eligible to vote) and **any()** to check if at least one person meets the condition. It’s a quick way to validate data in Python.                                    | [Voter Eligibility Checker](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/voter_eligibility_checker_github.py)       | Beginner      |
|`Simple Text Analysis with set() and len()`                | This code extracts unique words from a given text using the set() function and calculates their lengths. It creates a dictionary where keys are the unique words (case-insensitive) and values are their lengths. Simple, efficient, and useful!                                   | [analysis with set() and len()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/simple_text_analysis_github.py)       | Beginner      |
| `Simple Text Frequency Analysis with collections.Counter`                | This beginner-friendly Python program analyzes a given text to identify unique words and count their frequencies, using simple text-cleaning techniques and the powerful Counter function from the collections module.                                | [analysis with collections.Counter](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/analyze_frequency_github.py)    | Beginner      |
| ` List Comprehension`                | This program demonstrates the use of list comprehension, a powerful and concise way to create lists in Python. The code filters even numbers from 1 to (max values +1), calculates their squares, and stores the results in a single line of code. This is a practical example for scenarios where quick filtering and transformation of data are needed, such as generating specific numerical sequences or processing datasets.                     | [even number generator](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/even_square_generator_github.py)    | Beginner      |
| ` List And Dictionary Iteration`                |  A program that demonstrates iteration over a dictionary and a list, matching items from a shopping list with their prices in a price dictionary to calculate the total cost of the shopping.                  | [Grocery Shopping Helper](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/grocery_helper_iteration_github.py)    | Beginner      |
| `Dictionary Usage`                        |This code is Python program that converts distances between different units such as kilometers, miles, meters, and feet using a dictionary of conversion rates.                                     | [Unit Converter](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/unit_converter_github.py)       | Beginner  |
| `Dictionary Usage`                        |This program manages a list of students and their grades using a Python dictionary. It calculates and displays average grades for each student, demonstrates how to update data,adds new students and delete existing student. This example provides a foundational understanding of dictionary operations and their practical applications in real-world scenarios.                                      | [Grade Tracker](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/student_grade_tracker_github.py)       | Beginner  |
| `Dictionary Navigation Tools`                        | These methods provide efficient ways to access and iterate over the contents of a dictionary. .items() is ideal for working with both keys and values, .keys() focuses on the dictionary's keys, and .values() allows easy retrieval of all stored values.                                        | [Dict Navigation](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/dict_navigation_tools_github.py)       | Beginner  |
| `Dictionary Clear`                        | The clear() method removes all items from a dictionary, leaving it empty.                                        | [dict.clear()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/dict_clear_github.py)       | Beginner  |
| `Dictionary Update`                        | The update() function merges a dictionary with another dictionary or key-value pairs, adding new keys and updating existing ones.                                         | [dict.update()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/dict_update_github.py)       | Intermediate  |
| `Dictionary Unpack with ** and format()`                        | This is a code example that quickly unpacks dictionaries with the <b>**dict</b> statement and sends them as arguments to functions.                                         | [Unpack Dictinary with **](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/format_and_unpack_dict_github.py)       | Intermediate  |
| `Dictionary Fromkeys`                        | The fromkeys() function creates a new dictionary with specified keys and assigns a single value to all of them.                                         | [dict.fromkeys()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/dict_fromkeys_github.py)       | Intermediate  |
| `Dictionary Usage and get()`                        | This program uses dictionaries to compare the planned travel budget with the actual expenses for various categories (e.g., food, transport). It calculates and displays the remaining budget or overspending for each category, along with a total budget summary. The code demonstrates intermediate-level dictionary operations, including the get() method and dictionary comprehensions.                                       | [Travel Budget Tracker](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/travel_budget_tracker_dictionary_github.py)       | Intermediate  |
| `Dictionary And List Usage And defaultdict() `                        |This Python script organizes a list of names alphabetically by their first letter. It uses **defaultdict** to group names efficiently and displays the results in a clean, user-friendly format.                                 | [Auto-Sorting and Grouping Names by First Letter](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/auto_sorting_github.py)       | Intermediate  |
| `sort() , lambda And defaultdict() `                        | This program uses **defaultdict** from the **collections** module, a hidden gem in Python that allows you to avoid key errors by automatically initializing missing keys. In this case, it counts email domains in a list of email addresses, sorts them by frequency, and displays the results. It's a cool and practical tool for analyzing datasets containing email addresses! 🚀| [E-mail Domain Analysis](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/email_domain_analysis_github.py)       | Intermediate  |
| `Tuple`                        |This program uses tuples to manage and analyze weekly expenses for various categories. The budget and actual expenses are stored in tuples, and the program calculates whether each category stayed within the budget or not. It also provides a total summary of the budget vs. actual expenses.                                     | [Weekly Budget Tracker](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/weekly_budget_tracker_tuple_github.py)       | Intermediate  |
| `Lambda and filter()`                        | This script uses a lambda function and filter to identify credit card transactions exceeding a set spending limit. It demonstrates the practical application of functional programming for financial data analysis.                                       | [Spending Limit Control with lambda and filter()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/spending_limit_control_github.py)       | Intermediate  |
| `Condition Utils`                        | This code demonstrates how to use the any() and all() functions to evaluate conditions across an iterable. It checks whether at least one condition is met (any) or if all conditions are satisfied (all) within a list, tuple, or generator. These functions are particularly useful for concise and readable logical validations in Python.                                         | [Condition Utils](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/condition_utils.py)       | Intermediate  |
| `Useful Function - callable()`                        | This code demonstrates how callable() identifies objects or functions that can be invoked like functions, including instances of classes with a __call__ method.                                     | [callable()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/callable_github.py)       | Intermediate  |
| `Itertools Combination And Permutation`                        |  Use permutations and combinations from itertools to explore all possible orders and selections of elements.                                      | [Combination And Permutation](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/combination_and_permutation_github.py)       | Intermediate  |
| `Itertools Chain`                        | Demonstrates how itertools.chain flattens nested lists into a single iterable, showcasing its power in simplifying complex data structures.                    | [Chain](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/itertools_chain_github.py)       | Intermediate  |
| `Itertools Cycle`                        | The itertools.cycle function creates an infinite iterator that repeats the elements of a sequence in order, cycling back to the start when it reaches the end.                                     | [Cycle](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/circular_iteration.py)       | Intermediate  |
| `Itertools Product`                        | Generate all possible combinations of Turkish dishes, appetizer, and desserts using itertools.product for menu planning or brainstorming.                                     | [Product](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/itertools_product_github.py)       | Intermediate  |
| `Itertools Accumulate`                        |This script visualizes a business's daily income, expenses, and cumulative net income over a week. It calculates the daily net income by subtracting expenses from income, then computes the cumulative net total. The data is plotted using matplotlib, showing daily income, expenses, and cumulative net income with custom styling.                                     | [Accumulate- Sales Example](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/sales_calc_github.py)       | Intermediate  |
| `Itertools Reduce`                        |This code filters even numbers from a list using filter, calculates their squares with map, and sums the squares using reduce, demonstrating functional programming concepts in Python.                                   | [Reduce- Sum of Squared Even Numbers](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/itertools_reduce_github.py)       | Intermediate  |
| `Itertools next() and yield`                        |By combining the itertools next() function and the yield keyword, we created a simple animation that waits for the colors in the color array to play on the screen.               | [Simple Color Animation](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/itertools_and_yield_github.py)       | Intermediate  |
| ` yield`                        | This script creates a fun emoji-based animation using Python's yield. The emoji_animation generator cycles through a list of emojis, and the display_animation function controls the animation flow. The script uses \r to refresh the same line, creating a seamless visual effect.              | [Emoji Animation](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/emoji_animation_github.py)       | Intermediate  |
 `Generate Anagram`                        |This is a Python code that combines the useful functions itertools.permutations(), str.join(), str.strip(), and sorted() to find all anagrams of a given word.                                   | [Generate Anagrams](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/generate_anagrams_github.py)       | Intermediate  |
| `Memory Usage Check`                        | Examines memory consumption in Python programs                                           | [Memory Usage](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/memory_usage_check_github.py)       | Intermediate  |
| `Variables`                                 | Mutable objects can be modified after creation (e.g., lists, dictionaries), while immutable objects cannot be changed once created (e.g., strings, tuples).                               | [Mutable vs Immutable](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/mutable-immutable_github.py)       | Intermediate  |
| `is or ==`                                  | Explains identity (`is`) vs. equality (`==`) operators in Python                         | [== vs is](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/difference_between_%20%3D%3D_and%20_is_github.py)       | Intermediate  |
| `Merging Dictionaries`                      | Shows methods for combining dictionaries in Python                                       | [Merge Dictionaries](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/merge_dictionaries_github.py)       | Intermediate  |
| `Overriding Dictionaries`                      |      This script demonstrates how to combine menus from two restaurants using the \| operator in Python dictionaries. If an item exists in both menus, the price from the second menu overrides the first, creating a unified menu with the latest updates.                                | [Override Dictionaries](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/dict_override_github.py)       | Intermediate  |
| `Heap`                                      | Covers priority queues and heap data structures in Python                                | [Heap](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/heap_github.py)       | Intermediate  |
| `Flatten a list`                            | Techniques for unnesting nested lists                                                    | [Flatten A list](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/flatten_a_list_github.py)       | Intermediate  |
| `Fibonacci Generator with yield`                            | This code demonstrates two methods to generate the Fibonacci sequence: one using a list for storing all values (memory-intensive but straightforward) and another using a generator with yield to produce values on demand (memory-efficient and ideal for large sequences).                                                  | [Fibonacci Generator with yield](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/fib_generator_github.py)       | Intermediate  |
| `File Operations`                           | Basic file handling, including reading, writing, and managing files                      | [File Operations](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/tree/main/Open%20File%20With%20'with'%20And%20'strip()'%20Method)       | Intermediate  |
| `max() + collections.Counter()`                           | This Python script combines Counter for counting element frequencies and max with a custom key to efficiently find the most frequent element in a list.                    | [max() func](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/max_github.py)       | Intermediate  |
| `Class Method vs Static Method`                           |This example highlights the difference between @staticmethod for independent tasks and @classmethod for managing class-level data and behaviors.                 | [@classmethod vs @ staticmethod](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/classmethod_vs_staticmethod_github.py)       | Intermediate  |
| `Random Module`                           |This Python script generates a strong, random password using the string and random modules. It ensures the password is secure by including uppercase letters, lowercase letters, digits, and special characters. Users can define the length of the password, and the script guarantees unpredictability by shuffling the characters.| [Random Password Generator](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/random_password_generator_github.py)       | Intermediate  |
| `Random Module`                           |This code generates a random dream vacation plan by selecting a destination, activity, and duration. Every time you run the program, it creates a new unique vacation idea, adding a fun and inspiring touch to your day.| [Random Vacation Planner](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/random_vacation_planner_github.py)       | Intermediate  |
| `Ceasar Chipher`                           |The Caesar Cipher is one of the simplest and most famous encryption algorithms. It shifts each character in the alphabet by a fixed number of positions, creating an encrypted text that can be reversed with the same shift value.                | [Ceasar Cipher](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/ceasar_cipher_github.py)       | Intermediate  |
| ` filter(), lambda functions, and the := walrus operator `|This code is of intermediate level, utilizing advanced Python features such as filter(), lambda functions, and the := walrus operator. It demonstrates functional programming concepts, focusing on filtering valid email addresses by checking conditions like the presence of exactly one "@" symbol and a valid domain structure. Understanding these elements requires knowledge of Python's built-in functions and conditional expressions.            | [E-mail Validation](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/email_validation_filter_github.py)       | Intermediate  |
| ` := walrus operator `| This code showcases the assignment expression operator :=, also known as the "walrus operator," which allows assigning a value to a variable as part of an expression. Here, it is used to update the total_spent while simultaneously checking if it exceeds the budget, making the code more concise and readable.        | [Shopping Limit Tracker](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/shopping_limit_tracker_github.py)       | Intermediate  |
| `try - except and Errors `|   This script converts currencies safely using a dictionary of exchange rates. It demonstrates the use of try-except to handle errors such as missing exchange rates (KeyError), invalid inputs (ValueError), or unexpected errors (Exception). The finally block ensures a clean termination message is always shown, making it user-friendly.        | [Currency Converter](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/currency_converter_github.py)       | Intermediate  |
| `Useful Functions - enumerate(), pop(), append() and try-except)`             |This is a simple and interactive To-Do List Manager built with Python. It uses built-in list operations and functions like **sorted**, **append**, and **pop** to let users add, view, sort, and delete tasks, making task management easy and fun!                                   | [To Do List Manager](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/to_do_list_manager_github.py)       | Intermediate      |
| `Error Handling And datetime.now() And  timedelta()  `|   This script simulates a simple book borrowing system in a library. It uses Python's datetime module to calculate and display the borrowing and return dates. It also includes error handling to ensure valid user inputs.     | [Book Borrowing System](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/book_github.py)       | Intermediate  |
| `today.toordinal() + hash()`                                  | This program generates a personalized motivational quote based on the user's mood, leveraging datetime and random modules to ensure consistent results for the same date and mood combination.                                    | [Mood Quotes](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/mood_quotes_github.py)       | Advanced      |
| `Function`                                  | A first-class function is a function treated as a first-class citizen, meaning it can be passed as an argument, returned from another function, and assigned to a variable, just like any other object. This enables flexible and dynamic programming, allowing functions to be used as building blocks within other functions or data structures.                                     | [First Class Function](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/first_class_function_github.py)       | Advanced      |
| `Memoization`                               | A closure is a function that "remembers" the environment in which it was created, retaining access to variables from its containing scope even after that scope has finished executing. Closures are often used to create factory functions and encapsulate state.                    | [Closures](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/closures_github.py)       | Advanced      |
| `Effective Use Of Memory`                   | Generators are a type of iterable in Python that allow you to iterate over a sequence of values, but unlike lists, they generate values on the fly using yield, which makes them memory-efficient. Instead of storing the entire sequence in memory, they produce one item at a time as needed. This is particularly useful for working with large datasets.                              | [Generators](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/generators_github.py)       | Advanced      |
| `Useful Function - exec()`                  | The exec() function in Python dynamically executes Python code passed as a string. It can be used to run code that is generated or stored at runtime, making it powerful but also potentially risky, as it can execute arbitrary code. It's typically used for tasks like dynamic code execution or creating code templates.                                      | [exec()](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/exec.py)       | Advanced      |
| ` Vigenère Cipher `                  |This code implements the Vigenère Cipher, a polyalphabetic encryption method that uses a keyword to perform letter shifting. It handles both encryption and decryption of text while leaving non-alphabetic characters unaltered.                                  | [Vigenère Cipher](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/vigenere_github.py)       | Advanced      |
| ` Generators - send, next() and yield()`                  |     This code simulates a parking lot system using a Python generator. The parking_lot function uses yield to dynamically manage the parking spots, allowing cars to enter or exit in real-time while keeping track of the lot's state. It demonstrates how yield can pause and resume execution, making it perfect for scenarios like monitoring dynamic systems. The send() method enables communication with the generator, passing actions (like "enter" or "exit") to simulate real-world operations effectively.                 | [Vehicle Entry-Exit to the Parking Lot](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/vehicle_entry_exit_2_parking_lot_github.py)       | Advanced      |
| `Pathlib`                  | This script organizes files in any given folder into categorized subfolders based on their file extensions. It utilizes the pathlib library for robust and clean path handling. By categorizing files into pre-defined subfolders (e.g., Documents, Images, Videos), it offers a practical and efficient way to keep any directory well-organized with minimal effort. Simply point the script to the desired folder, and it will handle the rest!          | [File Organizer](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/file_organizer_github.py)       | Advanced      |
| `os module, psutil module, datetime module`                  | This Python script logs the square root of the system's uptime along with the current date and time to a file. It uses the **psutil** library for cross-platform uptime calculation, ensuring compatibility with both Windows and Linux systems.               | [System Performance Log](https://github.com/BetulKarakaya/Python-Tips-And-Tricks/blob/main/log_system_performance_github.py)       | Advanced      |




## Additional Resources

For more detailed information and resources on the topics covered in this repository, consider referring to the following sources:
- [Python 3.10.2 Documentation - Built-in Functions](https://docs.python.org/3/library/functions.html): Official documentation page for built-in functions in Python 3.10.2.

- [Python Documentation](https://docs.python.org/): Official Python documentation homepage for accessing additional resources and information.



## License
[MIT](https://choosealicense.com/licenses/mit/)
