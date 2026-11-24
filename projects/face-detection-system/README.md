
# Face Recognition Attendance System

A Python-based attendance management system that uses face recognition to identify students and automatically record their attendance.

## Features

- Real-time face detection using OpenCV.
- Face recognition using LBPH.
- Student registration and management.
- Automatic attendance marking.
- Prevention of duplicate attendance.
- Attendance report generation.
- Student attendance summary.
- Interactive command-line dashboard.

## Technologies Used

- Python
- OpenCV
- NumPy
- CSV
- Haar Cascade
- LBPH Face Recognizer

## Project Structure

```text
face-detection-system/
│
├── dashboard.py
├── main.py
├── student_management.py
├── capture_student.py
├── prepare_dataset.py
├── train_model.py
├── recognize_face.py
├── view_attendance.py
├── attendance_summary.py
└── README.md
```

## How to Run

1. Install the required libraries:

   pip install opencv-contrib-python==4.10.0.84 numpy

2. Run the dashboard:

   python dashboard.py

3. Select an option from the menu.

## How It Works

1. Register students.
2. Capture face images.
3. Process the captured images.
4. Train the face recognition model.
5. Recognize students through the webcam.
6. Automatically record attendance in a CSV file.

## Future Improvements

- Attendance percentage calculation.
- Graphical user interface.
- Export attendance reports to Excel.
- Improved recognition accuracy.

## Author

Created as a Python and OpenCV learning project.
