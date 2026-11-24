import csv
from collections import defaultdict

attendance_file = "attendance.csv"

attendance_count = defaultdict(set)

with open(attendance_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        date = row["Date"]

        attendance_count[name].add(date)

print("\n===== STUDENT ATTENDANCE SUMMARY =====\n")
print("{:<20} {:<20}".format("Student Name", "Days Present"))
print("-" * 40)

for name, dates in attendance_count.items():
    print("{:<20} {:<20}".format(name, len(dates)))

print("-" * 40)