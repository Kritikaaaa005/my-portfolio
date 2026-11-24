
import cv2
import os
import numpy as np

faces = []
labels = []

students = {
    0: "Student 1",
    1: "arjun"
}

for student_id in students:
    dataset_path = f"processed/student{student_id + 1}"

    for filename in os.listdir(dataset_path):
        image_path = os.path.join(dataset_path, filename)

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is not None:
            faces.append(image)
            labels.append(student_id)

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, np.array(labels))
recognizer.save("trainer.yml")

print("Model trained successfully!")

for student_id, name in students.items():
    print(name, "training images:", labels.count(student_id))

print("Total images:", len(faces))
