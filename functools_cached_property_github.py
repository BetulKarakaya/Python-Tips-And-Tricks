from functools import cached_property
import time

class WeatherFetcher:
    def __init__(self, city):
        self.city = city

    @cached_property
    def temperature(self):
    #his method runs when called for the first time and its result is stored (cached)
    #It does not run again in subsequent calls, the stored (pre-calculated) value is returned
    #So it is used as a property and also provides performance!
        start = time.time()
        print(f"Fetching temperature for {self.city}...")
        time.sleep(2)  # Simulate API
        return 24.5

    def __str__(self):
        return f"City: {self.city}"

def main():
    weather = WeatherFetcher("İstanbul")

    print("First access:")
    print(f"{weather.temperature}°C")

    print("\nSecond access (cached):")
    print(f"{weather.temperature}°C")

if __name__ == "__main__":
    main()
