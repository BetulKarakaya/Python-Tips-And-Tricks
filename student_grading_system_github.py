import statistics
import random
import matplotlib.pyplot as plt
import numpy as np

class StudentGradingSystem:
    def __init__(self, students):
        self.students = students  # {"Name": grade}
        self.mean = 0
        self.stdev = 0
        self.grades = {}

    def calculate_stats(self):
        grades = list(self.students.values())
        self.mean = statistics.mean(grades)
        self.stdev = statistics.stdev(grades)

    def assign_letter_grades(self):
        self.calculate_stats()
        for student, grade in self.students.items():
            if grade >= self.mean + 1.5 * self.stdev:
                self.grades[student] = 'A'
            elif grade >= self.mean + 0.5 * self.stdev:
                self.grades[student] = 'B'
            elif grade >= self.mean - 0.5 * self.stdev:
                self.grades[student] = 'C'
            elif grade >= self.mean - 1.5 * self.stdev:
                self.grades[student] = 'D'
            else:
                self.grades[student] = 'F'

    def visualize_grades(self):
        letter_grades = list(self.grades.values())
        grade_distribution = {grade: letter_grades.count(grade) for grade in set(letter_grades)}
        
        plt.bar(grade_distribution.keys(), grade_distribution.values(), color='skyblue')
        plt.title("Grade Distribution")
        plt.xlabel("Letter Grades")
        plt.ylabel("Number of Students")
        plt.yticks(np.arange(0,max(grade_distribution.values()) +1, 1))
        plt.grid()
        plt.gca().set_axisbelow(True)
        plt.show()

    def display_results(self):
        print(f"Class Average: {self.mean:.2f}")
        print(f"Standard Deviation: {self.stdev:.2f}\n")
        print("Student Grades:")
        for student, grade in self.grades.items():
            print(f"{student}: {grade}")


def main():
    random.seed(100)  # For consistent results
    students = {f"Student {i}": random.randint(0, 100) for i in range(1, 31)}  # 30 students with random grades

    grading_system = StudentGradingSystem(students)
    grading_system.assign_letter_grades()
    grading_system.display_results()
    grading_system.visualize_grades()

if __name__ == "__main__":
    main()