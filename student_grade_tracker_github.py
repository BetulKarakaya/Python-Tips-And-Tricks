# Student Grades Tracker

def calculate_average(grades):
    return sum(grades) / len(grades)

def display_average(dictionary_student):
    
    for student, grades in dictionary_student.items():
        # Calculate the average grade for the current student
        average = calculate_average(grades)

        # Print the student's name, grades, and average
        print(f"Student: {student}\nGrades: {grades}\nAverage: {average:.2f}\n")

if __name__ == "__main__":

    # Initialize a dictionary to store student names and their grades
    student_grades = {
        #student -> [grade1,grade2,grade3]
        "John": [85, 90, 88],  
        "Sarah": [78, 82, 80],  
        "Jacob": [92, 85, 87] 
    }
    
    # Display student grades and their average
    display_average(student_grades)

    # Add a new student and their grades
    student_grades["Elizabeth"] = [88, 91, 85]  # Adding Diana to the dictionary

    # Update grades for an existing student
    student_grades["John"][0] = 89  # Update John's first grade

    # Delete an existing student
    student_grades.pop("Jacob")  

    # Display the updated dictionary
    display_average(student_grades)