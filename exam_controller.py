from exam_service import ExamService

class ExamController:
    def __init__(self):
        self.service = ExamService()

    def start_portal(self):
        while True:
            print("\n---- Student Exam Portal ----")
            print("1. Add Student")
            print("2. Add Exam")
            print("3. Submit Marks")
            print("4. View Student Report")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.service.add_student()
            elif choice == '2':
                self.service.add_exam()
            elif choice == '3':
                self.service.submit_marks()
            elif choice == '4':
                self.service.view_report()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
