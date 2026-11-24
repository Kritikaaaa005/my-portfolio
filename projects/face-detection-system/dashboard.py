
import os

def show_menu():
    while True:
        print("\n===================================")
        print("  FACE RECOGNITION ATTENDANCE SYSTEM")
        print("===================================")

        print("1. Register a Student")
        print("2. Capture Student Face")
        print("3. Train Recognition Model")
        print("4. Start Attendance")
        print("5. View Attendance Report")
        print("6. View Attendance Summary")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            os.system("python student_management.py")

        elif choice == "2":
            os.system("python capture_student.py")

        elif choice == "3":
            os.system("python train_model.py")

        elif choice == "4":
            os.system("python recognize_face.py")

        elif choice == "5":
            os.system("python view_attendance.py")

        elif choice == "6":
            os.system("python attendance_summary.py")

        elif choice == "7":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Please try again.")


show_menu()
