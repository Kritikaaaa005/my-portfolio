
import cv2
import csv
import os

# Load student details
students = {}

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students[int(row["Student_ID"])] = row["Student_Name"]

# Ask for student ID
student_id = int(input("Enter Student ID: "))

if student_id not in students:
    print("Student not found!")
    exit()

student_name = students[student_id]

# Create student dataset folder
folder_name = f"dataset/student{student_id + 1}"
os.makedirs(folder_name, exist_ok=True)

# Load face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

camera = cv2.VideoCapture(0)
count = 0

print("Capturing face images for:", student_name)
print("Press S to save an image and Q to quit.")

while True:
    success, frame = camera.read()

    if not success:
        print("Could not access webcam.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.putText(
        frame, f"Images: {count}", (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
    )

    cv2.imshow("Capture Student Face", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        if len(faces) > 0:
            x, y, w, h = max(faces, key=lambda face: face[2] * face[3])
            face_image = gray[y:y+h, x:x+w]

            count += 1
            image_path = os.path.join(folder_name, f"{count}.jpg")
            cv2.imwrite(image_path, face_image)

            print("Saved image:", count)
        else:
            print("No face detected!")

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print("Total images captured:", count)
