class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("❌ Celsius value must be a number.")
        return round((celsius * 9/5) + 32, 2)

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("❌ Fahrenheit value must be a number.")
        return round((fahrenheit - 32) * 5/9, 2)

def main():
    print("Let's do some clean conversions!".center(80,"-"))

    c = 25
    f = TemperatureConverter.celsius_to_fahrenheit(c)
    print(f"🔹 {c}°C → {f}°F")

    f = 98.6
    c = TemperatureConverter.fahrenheit_to_celsius(f)
    print(f"🔹 {f}°F → {c}°C")


if __name__ == "__main__":
    main()