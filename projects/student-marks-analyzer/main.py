def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


print("===== Student Marks Analyzer =====")

name = input("Enter student name: ")
subjects = int(input("Enter the number of subjects: "))
marks = []

for i in range(1, subjects+1):
    while True:
        score = float(input(f"Enter marks for subject {i} (out of 100): "))

        if 0 <= score <= 100:
            marks.append(score)
            break
        else:
            print("Please enter marks between 0 and 100.")

total = sum(marks)
percentage = total / len(marks)
grade = calculate_grade(percentage)

outOf = subjects*100
print("\n===== Result =====")
print("Student:", name)
print("Total Marks:", total, "/",outOf)
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)