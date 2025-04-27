class WeatherBaseActivity:
    weather_dict = {
        1: "Sunny",
        2: "Mildly",
        3: "Cloudy",
        4: "Windy",
        5: "Rainy",
        6: "Snowy",
        7: "Too Cold",
        8: "Too Hot",
        9: "Stormy"
    }

    def __init__(self, input_choice: int):
        self.weather = self.weather_dict.get(input_choice, "Else").lower()

    def suggest(self):
        if self.weather in ("sunny", "cloudy", "mildly"):
            print("😎 Let's go for a walk!")
        elif self.weather in ("rainy", "snowy", "windy"):
            print("☔ Weather can be moody... Perfect time to journal, draw or read!")
        elif self.weather in ("too cold", "too hot", "stormy"):
            print("☕ Stay inside, grab a cozy drink and enjoy a movie!")
        else:
            print("🤔 Hmm, that's an interesting weather!")

    @staticmethod
    def display_weather_dict():
        for i, weather in WeatherBaseActivity.weather_dict.items():
            print(f"{i} ---> {weather}")

def main():
    print("✨ Welcome to the Weather-Based Activity App! Here's your options:\n")
    WeatherBaseActivity.display_weather_dict()

    try:
        choice = int(input("\n🌦️ How is the weather today? (Enter number like 1, 5, etc.): "))
        app = WeatherBaseActivity(choice)
        app.suggest()
    except ValueError:
        print("❌ Invalid input. Please enter a valid number!")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
