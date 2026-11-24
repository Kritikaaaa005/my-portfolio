import csv
import os

attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):
    print("No attendance records found.")

else:
    with open(attendance_file, "r") as file:
        reader = csv.DictReader(file)

        print("\n===== ATTENDANCE REPORT =====\n")
        print("{:<20} {:<15} {:<15}".format("Student Name", "Date", "Time"))
        print("-" * 50)

        count = 0

        for row in reader:
            print("{:<20} {:<15} {:<15}".format(
                row["Name"], row["Date"], row["Time"]
            ))
            count += 1

        print("-" * 50)
        print("Total attendance records:", count)