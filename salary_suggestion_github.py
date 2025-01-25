
class Employee:
    def __init__(self, name, department, salary, overtime_hours):
        self.name = name
        self.department = department
        self.salary = salary
        self.overtime_hours = overtime_hours

def main():
    employees = [
        Employee(name="Ali Yılmaz", department="IT", salary=27000, overtime_hours=15),
        Employee(name="Ayşe Demir", department="HR", salary=45000, overtime_hours=8),
        Employee(name="Mehmet Kaya", department="Finance", salary=62000, overtime_hours=2),
    ]


    suggest_salary_update = list(map(lambda emp: emp.salary * 1.10 if emp.overtime_hours >= 5 else emp.salary, employees))


    for i, employee in enumerate(employees):
        print(
            f"Name: {employee.name}, "
            f"Department: {employee.department}, "
            f"Salary: {employee.salary} TL, "
            f"Overtime Hours: {employee.overtime_hours}, "
            f"New Salary Suggestion: {suggest_salary_update[i]:.2f} TL"
        )

if __name__ == "__main__":
    main()