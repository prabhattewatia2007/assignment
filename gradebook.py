#----------------------------------------------------------
# Name: Prabhat Tewatia
# Date: 11-Nov-2025
# Project: GradeBook Analyzer
# ----------------------------------------------------------

print("===================================")
print(" Welcome to the GradeBook Analyzer ")
print("===================================\n")
print("This program helps teachers analyze student marks and grades.\n")
# Step 1: Take input for number of students
num_students = int(input("Enter the number of students: "))

# Step 2: Create a dictionary to store marks
marks = {}

# Step 3: Collect data for each student
for i in range(num_students):
    name = input(f"Enter name of student {i+1}: ")
    score = float(input(f"Enter marks of {name}: "))
    marks[name] = score

print("\nAll student marks recorded successfully!\n")
{"Alice": 78, "Bob": 92, "Carol": 56}
# --- Functions for statistics ---

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    n = len(scores)
    if n % 2 == 0:
        return (scores[n//2 - 1] + scores[n//2]) / 2
    else:
        return scores[n//2]

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

# --- Calling the functions ---
average = calculate_average(marks)
median = calculate_median(marks)
highest = find_max_score(marks)
lowest = find_min_score(marks)

print("Class Statistics:")
print(f"Average Marks: {average:.2f}")
print(f"Median Marks: {median:.2f}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}\n")
# --- Grade Assignment ---
grades = {}

for name, score in marks.items():
    if score >= 90:
        grades[name] = 'A'
    elif score >= 80:
        grades[name] = 'B'
    elif score >= 70:
        grades[name] = 'C'
    elif score >= 60:
        grades[name] = 'D'
    else:
        grades[name] = 'F'

# --- Count number of students in each grade ---
grade_counts = {}
for grade in grades.values():
    grade_counts[grade] = grade_counts.get(grade, 0) + 1

print("Grade Distribution:")
for grade, count in grade_counts.items():
    print(f"{grade}: {count} student(s)")
print()
# --- Pass/Fail using list comprehension ---
passed_students = [name for name, score in marks.items() if score >= 40]
failed_students = [name for name, score in marks.items() if score < 40]

print("Pass/Fail Summary:")
print(f"Passed Students ({len(passed_students)}): {passed_students}")
print(f"Failed Students ({len(failed_students)}): {failed_students}\n")
# --- Function to display results table ---
def display_results_table(marks_dict, grades_dict):
    print("\nStudent Results:")
    print("Name\t\tMarks\tGrade")
    print("----------------------------------")
    for name in marks_dict:
        print(f"{name}\t\t{marks_dict[name]}\t{grades_dict[name]}")
    print("----------------------------------\n")

# --- Main program loop ---
while True:
    display_results_table(marks, grades)
    choice = input("Do you want to re-run the analysis? (yes/no): ").lower()
    if choice == "yes":
        print("\nRestarting...\n")
        # You could optionally re-run the data entry part again
        break  # For simplicity, you can remove this if you rebuild fully
    else:
        print("Thank you for using GradeBook Analyzer. Goodbye!")
        break
===================================
 Welcome to the GradeBook Analyzer 
===================================

This program helps teachers analyze student marks and grades.

Enter the number of students: 5
Enter name of student 1: Alice
Enter marks of Alice: 78
Enter name of student 2: Bob
Enter marks of Bob: 92
Enter name of student 3: Carol
Enter marks of Carol: 56
Enter name of student 4: David
Enter marks of David: 84
Enter name of student 5: Eva
Enter marks of Eva: 39

All student marks recorded successfully!

Class Statistics:
Average Marks: 69.80
Median Marks: 78.00
Highest Marks: 92.0
Lowest Marks: 39.0

Grade Distribution:
A: 1 student(s)
B: 1 student(s)
C: 1 student(s)
D: 1 student(s)
F: 1 student(s)

Pass/Fail Summary:
Passed Students (4): ['Alice', 'Bob', 'Carol', 'David']
Failed Students (1): ['Eva']

Student Results:
Name        Marks   Grade
----------------------------------
Alice       78.0    C
Bob         92.0    A
Carol       56.0    F
David       84.0    B
Eva         39.0    F
----------------------------------

Do you want to re-run the analysis? (yes/no): no
Thank you for using GradeBook Analyzer. Goodbye!
