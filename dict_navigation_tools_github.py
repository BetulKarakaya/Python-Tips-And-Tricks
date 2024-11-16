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

    # .items(): Returns a view object containing key-value pairs as tuples. 
    # Useful for iterating through both keys and values.
    print(employee.items())  
    # Output: dict_items([('employee_id', 12345), ('name', 'Jane Doe'), 
    # ('position', 'Software Engineer'), ('department', 'R&D'), ('salary', 85000), 
    # ('email', 'jane.doe@example.com'), ('start_date', '2022-03-15'), ('is_full_time', True),
    # ('skills', ['Python', 'SQL']), ('performance_scores', {'2022': 8.5, '2023': 9.0, '2024': 9.2}), ('manager', 'Jane Smith')])
    
    
    # .keys(): Returns a view object containing all the keys in the dictionary. 
    # Useful when you need only the keys.
    print(employee.keys())  
    # Output: dict_keys(['employee_id', 'name', 'position', 'department', 'salary',
    # 'email', 'start_date', 'is_full_time', 'skills', 'performance_scores', 'manager'])
    

    # .values(): Returns a view object containing all the values in the dictionary. 
    # Useful when you need only the values.
    print(employee.values())  
    # Output: dict_values([12345, 'Jane Doe', 'Software Engineer', 'R&D', 85000, 'jane.doe@example.com', 
    # '2022-03-15', True, ['Python', 'SQL'], {'2022': 8.5, '2023': 9.0, '2024': 9.2}, 'Jane Smith'])
    

