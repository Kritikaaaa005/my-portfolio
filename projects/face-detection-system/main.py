import cv2
import os

camera = cv2.VideoCapture(0)

save_path = "dataset/student1"

count = 0

while True:
    success, frame = camera.read()

    if not success:
        print("Camera error!")
        break

    cv2.imshow("Capture Student Images", frame)

    key = cv2.waitKey(1)

    # Press S to save an image
    if key == ord('s'):
        count += 1

        file_name = os.path.join(save_path, f"{count}.jpg")
        cv2.imwrite(file_name, frame)

        print("Image saved:", file_name)

    # Press Q to exit
    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()