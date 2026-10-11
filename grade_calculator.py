def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1 (0-100): "))
mark2 = float(input("Enter marks for Subject 2 (0-100): "))
mark3 = float(input("Enter marks for Subject 3 (0-100): "))

if not all(0 <= mark <= 100 for mark in [mark1, mark2, mark3]):
    print("Invalid marks! Enter marks between 0 and 100.")
else:
    average = (mark1 + mark2 + mark3) / 3
    grade = calculate_grade(average)

    print("\n===== RESULT =====")
    print("Student:", name)
    print("Average:", round(average, 2))
    print("Grade:", grade)

    if min(mark1, mark2, mark3) < 40:
        print("Status: Needs improvement")
    else:
        print("Status: Passed")