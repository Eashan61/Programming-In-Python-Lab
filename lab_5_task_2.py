students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

#task 1 return average marks
def calculate_average(marks):
    if len(marks) == 0:
        return None  # Prevents division by zero if marks list is empty

    total = 0
    for m in marks:
        # Marks must be between 0 and 100
        if m < 0 or m > 100:
            return None  # Invalid mark detected
        total += m

    average = total / len(marks)
    return average

#task 2 return performance catagory based on the average
def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average > 70:   # Note: Use >= 70 if your instructor counts 70 as Good
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

# Task 3: Display each student's ID, name, average, and performance category
def display_report(students):
    print("Student Performance Report:")

    if len(students) == 0:
        print("Student list is empty.")
        return

    for student in students:
        student_id = student[0]
        name = student[1]
        marks = student[2]

        # Check 1: Missing marks (empty list)
        if len(marks) == 0:
            print(f"ID: {student_id}\nName: {name}\nStatus: Error - No marks recorded!\n")
            continue

        # Calculate average 
        avg = calculate_average(marks)

        # Check 2: Invalid mark (< 0 or > 100)
        if avg is None:
            print(f"ID: {student_id}\nName: {name}\nMarks: {marks}\nStatus: Error - Invalid mark found (must be between 0 and 100)!\n")
            continue

        category = classify_performance(avg)
        print(f"ID: {student_id}\nName: {name}\nAverage: {avg:.2f}\nCategory: {category}\n")

# 1. Run report on the standard sample data
display_report(students)

# 2. Testing & Debugging Cases
test_students = [
    [205, "Tania", [80, 80, 80]],       # Case 1: Equal marks in all assessments (Avg: 80.00)
    [206, "Karim", [70, 80, 90]],       # Case 2: Tied average with Tania (Avg: 80.00)
    [207, "Sadia", [85, 110, 90]],      # Case 3: Invalid mark (> 100)
    [208, "Fahim", [-10, 75, 80]],      # Case 3: Invalid mark (< 0)
    [209, "Rafi", []]                   # Case 4: Student record with no marks
]

print("\nRunning Testing & Debugging Cases")
display_report(test_students)