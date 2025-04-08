from collections import namedtuple, ChainMap

# Define a fixed structure for student data using namedtuple
Student = namedtuple('Student', ['name', 'age', 'grade'])

class SchoolRecords:
    def __init__(self):
        # Main records from the school's primary database
        self.primary_records = {
            "101": Student("Alice", 14, "8th"),
            "102": Student("Bob", 15, "9th")
        }

        # Updated records from recent data collection (e.g., grade change)
        self.updated_records = {
            "102": Student("Bob", 15, "10th"),  # Bob moved to 10th grade
            "103": Student("Charlie", 13, "7th")  # New student
        }

        # Merge both sources with ChainMap (updated data has priority)
        self.all_records = ChainMap(self.updated_records, self.primary_records)

    def get_student_info(self, student_id):
        #Returns structured student info if available.
        return self.all_records.get(student_id, "⚠️ Student Not Found")

    def display_all_students(self):
        #Displays all student records in a formatted table.

        print(f"{'ID':^6}|{'Name':^12}|{'Age':^6}|{'Grade':^8}")
        print("-" * 36)
        
        # Collect unique IDs across both dictionaries
        all_ids = set(self.primary_records.keys()) | set(self.updated_records.keys())

        for student_id in sorted(all_ids):
            data = self.all_records.get(student_id, None)
            if data:
                print(f"{student_id:^6}|{data.name:^12}|{data.age:^6}|{data.grade:^8}")
            else:
                print(f"{student_id:^6}|{'-':^12}|{'-':^6}|{'-':^8}")

def main():
    school = SchoolRecords()
    school.display_all_students()

    print("\n🔹 Querying Student Info:")
    print("102:", school.get_student_info("102"))  # Updated Bob
    print("104:", school.get_student_info("104"))  # Not Found

if __name__ == "__main__":
    main()
