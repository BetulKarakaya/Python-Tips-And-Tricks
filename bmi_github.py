class InvalidWeightError(Exception):
    def __init__(self, weight):
        super().__init__(f"Invalid Weight: {weight} kg. Weight must be between 1kg and 300kg")
    
class InvalidHeightError(Exception):
    def __init__(self, height):
        super().__init__(f"Invalid Height: {height} m. Height must be between 0.1m and 2.20 m")

class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid Age: {age} . Age must be between 1 and 120")

class InvalidGenderError(Exception):
    def __init__(self, gender):
        super().__init__(f"Invalid Gender: {gender} . Gender must be Female or Male")

class BMI_Calculator:
    def __init__(self, weight, height, age, gender):
        
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
    

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def calculate_body_fat_percentage(self):
        if self.gender.lower() == "male":
            return 1.20 * self.bmi + 0.23 * self.age - 16.2
        elif self.gender.lower() == "female":
            return 1.20 * self.bmi + 0.23 * self.age - 5.4

    def classify_bmi(self):
        # Determines gender-specific BMI category
        
        if self.gender.lower() == "male":
            if self.bmi < 18.5:
                return "Underweight"
            elif self.bmi < 25:
                return "Normal weight"
            elif self.bmi < 30:
                return "Overweight"
            elif self.bmi < 35:
                return "Obese (Class 1)"
            elif self.bmi < 40:
                return "Obese (Class 2)"
            else:
                return "Obese (Class 3) (Morbidly Obese)"
        
        elif self.gender.lower() == "female":
            if self.bmi < 18.0:
                return "Underweight"
            elif self.bmi < 24.5:
                return "Normal weight"
            elif self.bmi < 30:
                return "Overweight"
            elif self.bmi < 35:
                return "Obese (Class 1)"
            elif self.bmi < 40:
                return "Obese (Class 2)"
            else:
                return "Obese (Class 3) (Morbidly Obese)"
        else:
            return "Invalid gender"

    def classify_body_fat(self):
        # Evaluates Body Fat Percentage According to US Navy Standard
        if self.gender.lower() == "male":
            if self.body_fat < 6:
                return "Essential Fat"
            elif self.body_fat < 14:
                return "Athletic"
            elif self.body_fat < 18:
                return "Fit"
            elif self.body_fat < 25:
                return "Average"
            else:
                return "Obese"
        
        elif self.gender.lower() == "female":
            if self.body_fat < 14:
                return "Essential Fat"
            elif self.body_fat < 21:
                return "Athletic"
            elif self.body_fat < 25:
                return "Fit"
            elif self.body_fat < 32:
                return "Average"
            else:
                return "Obese"

    def calculation(self):
        self.bmi = self.calculate_bmi()
        self.body_fat = self.calculate_body_fat_percentage()
        self.category = self.classify_bmi()
        self.body_fat_category = self.classify_body_fat()

    def print_results(self):
        print(f"\n📌 BMI Value: {self.bmi:.2f}")
        print(f"📌 Body Fat Percentage: {self.body_fat:.2f}%")
        print(f"📌 BMI Category: {self.category}")
        print(f"📌 US Navy Fat Content Your Category: {self.body_fat_category}")


def main():
    
    weight = float(input("Enter Your Weight (kg): "))
    if weight < 1 or weight > 300:
        raise InvalidWeightError(weight = weight)
    
    height = float(input("Enter Your Height (meter): "))
    if height < 0.1 or height > 2.20:
        raise InvalidHeightError(height = height)
    
    age = int(input("Enter Your Age: "))
    if age < 1 or age > 120:
        raise InvalidAgeError(age = age)
    
    gender = input("Enter Your Gender (Male/Female): ").lower()
    if gender not in ["female", "male"]:
        raise InvalidGenderError(gender = gender)
    

    app = BMI_Calculator(height= height, weight= weight, age= age, gender= gender)
    app.calculation()
    app.print_results()

if __name__ == "__main__":
    main()
