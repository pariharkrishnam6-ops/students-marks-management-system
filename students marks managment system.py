print("===== STUDENT MARKS MANAGEMENT SYSTEM =====")

name = input("Enter student name: ")

while True:
    try:
        num_subjects = int(input("Enter number of subjects: "))
        if num_subjects > 0:
            break
        print("Please enter a number greater than zero.")
    except ValueError:
        print("Please enter a valid whole number.")

subjects = []
marks = []

for i in range(num_subjects):
    subject = input(f"\nEnter subject {i } name: ")

    while True:
        try:
            mark = float(input(f"Enter marks for {subject}: "))

            if 0 <= mark <= 100:
                break

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter valid numeric marks.")

    subjects.append(subject)
    marks.append(mark)

total = sum(marks)
average = total / num_subjects
highest = max(marks)
lowest = min(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

if all(mark >= 40 for mark in marks):
    result = "PASS"
else:
    result = "FAIL"

print("\n========== STUDENT REPORT ==========")
print("Student Name:", name)

print("\nSubject-wise Marks:")

for i in range(num_subjects):
    print(subjects[i], ":", marks[i])

print("\nTotal Marks:", total)
print("Average:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Grade:", grade)
print("Final Result:", result)

print("====================================")