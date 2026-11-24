
import cv2
import csv
import os
from datetime import datetime

# Load student records
students = {}

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students[int(row["Student_ID"])] = row["Student_Name"]

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

attendance_file = "attendance.csv"
marked_names = set()

def mark_attendance(name):

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    # Check whether attendance already exists today
    if os.path.exists(attendance_file):
        with open(attendance_file, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Name"] == name and row["Date"] == today:
                    print(name, "already marked today!")
                    return

    # Save attendance
    file_exists = os.path.exists(attendance_file)

    with open(attendance_file, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(attendance_file) == 0:
            writer.writerow(["Name", "Date", "Time"])

        writer.writerow([name, today, current_time])

    print("Attendance marked for", name)


camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        print("Camera error!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label, confidence = recognizer.predict(face)

        if label in students and confidence < 70:

            name = students[label]
            color = (0, 255, 0)

            if name not in marked_names:
                mark_attendance(name)
                marked_names.add(name)

        else:
            name = "Unknown"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        cv2.putText(
            frame, name, (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2
        )

    cv2.imshow("Face Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
