class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                self.grades.append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def __str__(self):
        avg = self.average()
        return f"{self.name}: Grades = {self.grades}, Average = {avg:.2f}"

def main():
    students = {}

    while True:
        print("\n--- Student Grade Tracker ---")
        print("1. Add student")
        print("2. Add grade")
        print("3. View student report")
        print("4. View all students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            if name in students:
                print("Student already exists.")
            else:
                students[name] = Student(name)
                print(f"Student '{name}' added.")

        elif choice == '2':
            name = input("Enter student name: ")
            if name in students:
                grade = input("Enter grade (0–100): ")
                students[name].add_grade(grade)
            else:
                print("Student not found.")

        elif choice == '3':
            name = input("Enter student name: ")
            if name in students:
                print(students[name])
            else:
                print("Student not found.")

        elif choice == '4':
            if not students:
                print("No students added yet.")
            else:
                for student in students.values():
                    print(student)

        elif choice == '5':
            print("Exiting Grade Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the tracker
main()
