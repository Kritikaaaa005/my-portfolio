import csv
import os

file_name = "students.csv"

def add_student():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    students = {}

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students[row["Student_ID"]] = row["Student_Name"]

    if student_id in students:
        print("Student ID already exists!")

    else:
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)

            if os.path.getsize(file_name) > 0:
                file.write("\n")

            writer.writerow([student_id, student_name])

        print("Student added successfully!")


def view_students():
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        print("\n===== REGISTERED STUDENTS =====")

        for row in reader:
            print(row["Student_ID"], "-", row["Student_Name"])


while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")