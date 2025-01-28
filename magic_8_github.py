import random

def magic_8_ball():
    # List of possible answers
    responses = [
        "Yes, definitely!",
        "It is certain.",
        "Without a doubt.",
        "Most likely.",
        "Ask again later.",
        "Cannot predict now.",
        "Don't count on it.",
        "My reply is no.",
        "Very doubtful.",
        "Outlook not so good."
    ]
    
    print("🎱 Welcome to the Magic 8-Ball! 🎱")
    
    while True:
        question = input("\nAsk a 'Yes' or 'No' question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            print("Goodbye! Hope to see you again. 🎱")
            break
        
        if not question.endswith("?"):
            print("That's not a question! Please ask properly ending with a '?'.")
        else:
            # Randomly choose an answer
           
            answer = random.choice(responses)
            print(f"🔮 The Magic 8-Ball says: {answer}")

if __name__ == "__main__": 
    random.seed(40)
    magic_8_ball()
