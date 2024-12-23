import time

def emoji_animation(emojis):
    """
    A generator function that cycles through emojis to create a simple animation effect.
    """
    
    while True:
        for emoji in emojis:
            yield emoji  # Generate the next emoji in the sequence

def display_animation(generator, emojis, cycles=3):
    """
    Displays the emoji animation for a specified number of cycles.
    """
    print("🎬 Starting Emoji Animation 🎬\n")
    for _ in range(cycles * len(emojis)):  # Multiply cycles by the number of emojis
        print(f"\r{next(generator)}", end="", flush=True)  # Update the same line with the next emoji
        time.sleep(0.3)  # Add a small delay to simulate animation
    print("\n\n✨ Animation Complete! ✨")

if __name__ == "__main__":
    emojis = ["😀", "😂", "😎", "🤔", "😴", "🤩", "🥳", "❤️", "🔥", "🌟"]
    # Create the emoji animation generator
    emoji_gen = emoji_animation(emojis)
    
    # Display the animation
    display_animation(emoji_gen,emojis)
