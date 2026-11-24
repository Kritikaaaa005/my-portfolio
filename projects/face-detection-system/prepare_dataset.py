
import cv2
import os

dataset_path = "dataset/student2"
output_path = "processed/student2"

os.makedirs(output_path, exist_ok=True)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0

for filename in os.listdir(dataset_path):
    image_path = os.path.join(dataset_path, filename)

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        continue

    faces = face_detector.detectMultiScale(
        image, scaleFactor=1.3, minNeighbors=5
    )

    if len(faces) > 0:
        x, y, w, h = max(faces, key=lambda face: face[2] * face[3])

        face = image[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        count += 1
        cv2.imwrite(
            os.path.join(output_path, f"{count}.jpg"),
            face
        )

print("Arjun's images processed:", count)
