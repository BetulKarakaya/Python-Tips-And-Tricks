if __name__ == "__main__":

    employee = {
    "employee_id": 12345,
    "name": "Jane Doe",
    "position": "Software Engineer",
    "department": "R&D",
    "salary": 85000,
    "email": "jane.doe@example.com",
    "start_date": "2022-03-15",
    "is_full_time": True,
    "skills": ["Python","SQL"],
    "performance_scores": {"2022": 8.5, "2023": 9.0, "2024": 9.2},
    "manager": "Jane Smith"
    }
    print(employee)# 
    # Explanation: Clears all key-value pairs from the dictionary.
    employee.clear()
    print(employee)  # Output: {}
       
