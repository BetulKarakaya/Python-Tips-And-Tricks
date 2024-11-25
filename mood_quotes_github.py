import random
from datetime import datetime

def generate_motivational_quote(mood):
    """
    Generates a motivational quote based on the user's mood.
    
    Parameters:
        mood (str): User's mood ('sad', 'tired', 'hopeless', 'happy', etc.)
    
    Returns:
        str: A motivational quote tailored to the mood.
    """
    # Define mood-based quotes
    mood_quotes = {
        "sad": [
            "It's okay to feel sad, but don't forget the sun always shines after the storm.",
            "Cry if you must, but never lose hope. Tomorrow is a new day.",
            "Even the darkest night will end, and the sun will rise.",
        ],
        "tired": [
            "Rest if you must, but don't you quit!",
            "Take a deep breath. Small steps lead to big achievements.",
            "It's okay to be tired. Just remember why you started.",
        ],
        "hopeless": [
            "Hope is being able to see that there is light despite all the darkness.",
            "You are stronger than you think. Keep believing in yourself.",
            "Every failure is a step closer to success. Don't give up.",
        ],
        "happy": [
            "Keep spreading your joy; it's contagious!",
            "Happiness is not something ready-made. It comes from your own actions.",
            "Life is better when you're laughing. Keep it up!",
        ],
        "default": [
            "Believe in yourself and all that you are.",
            "Push yourself because no one else is going to do it for you.",
            "Success doesn't come from what you do occasionally; it comes from what you do consistently.",
        ],
    }

    # Get quotes for the specified mood or use default if mood not found
    quotes = mood_quotes.get(mood.lower(), mood_quotes["default"])
    
    # Seed random generator with today's date for consistency   
    
    # datetime.now().date(): Determines today's date.
    
    # today.toordinal(): Represents today as a number. 
    # datetime.date(2024, 11, 24).toordinal() => 738870
    # In other words, exactly 738,870 days have passed since January 1, Year 1.
    
    # hash(mood): The user's mood is converted into a number.
    
    # The sum of the two creates a unique seed for randomness. 
    # In this way, the same result is produced for the same combination of date and mood.
    today = datetime.now().date()
    random.seed(today.toordinal() + hash(mood))  # Combine date and mood for unique quote
    
    # Select a random quote
    return random.choice(quotes)

if __name__ == "__main__":
    # Ask user for their current mood
    print("🌟 Welcome to the Mood-Based Motivational Quote Generator! 🌟")
    user_mood = input("How are you feeling today? (e.g., sad, tired, hopeless, happy): ").strip()

    # Generate and print the quote
    print(f"\n🌈 Your Mood-Based Motivational Quote 🌈")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"💡 {generate_motivational_quote(user_mood)}")
