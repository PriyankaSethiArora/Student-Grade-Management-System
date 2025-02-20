import csv  
import os

STUDENT_DATA_FILE = "students.csv"

# Function to load students from a file
def load_students():
    students = {}
    try:
        with open(STUDENT_DATA_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print("Loaded row:", row)  # Debugging print statement
                if len(row) > 1:
                    name, grades = row[0], []
                    try:
                        grades = [float(g) for g in row[1:] if g.replace('.', '', 1).isdigit()]
                    except ValueError:
                        print(f"Skipping invalid data for student {name}.")
                    students[name] = grades
    except FileNotFoundError:
        print("File not found, starting with empty data.")
    return students

# Function to save students to a file
def save_students(students):
    print("Attempting to save students:", students)  # Debugging print
    try:
        with open(STUDENT_DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            for name, grades in students.items():
                writer.writerow([name] + grades)
        print("Data saved successfully!")  # Debugging print
    except Exception as e:
        print(f"Error saving file: {e}")

# Function to add a new student
def add_student(students):
    name = input("Enter student name: ").strip().title()
    
    while True:
        grades_input = input("Enter grades separated by spaces: ").split()
        try:
            grades = [float(g) for g in grades_input]
            students[name] = grades
            save_students(students)
            print(f"Student {name} added successfully.")
            break
        except ValueError:
            print("Invalid input! Kindly enter numbers only.")

# Function to calculate the average grade of a student
def calculate_average(students):
    name = input("Enter student name: ").strip().title()
    if name in students and students[name]:
        avg = sum(students[name]) / len(students[name])
        print(f"{name}'s average grade: {avg:.2f}")
    else:
        print("Student not found or has no valid grades.")

# Function to find the highest and lowest scoring students
def find_extremes(students):
    if not students:
        print("No students available.")
        return
    
    averages = {name: sum(grades) / len(grades) for name, grades in students.items() if grades}
    if not averages:
        print("No valid grades found.")
        return
    
    highest = max(averages, key=averages.get)
    lowest = min(averages, key=averages.get)

    print(f"Highest scoring student: {highest} with {averages[highest]:.2f}")
    print(f"Lowest scoring student: {lowest} with {averages[lowest]:.2f}")

# Main function to display menu and handle user input
def main():
    students = load_students()
    
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Calculate Average Grade")
        print("3. Find Highest and Lowest Scoring Students")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            calculate_average(students)
        elif choice == '3':
            find_extremes(students)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
