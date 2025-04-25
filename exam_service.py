from student import Student
from exam import Exam

class ExamService:
    def __init__(self):
        self.students = {}
        self.exams = {}

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        self.students[student_id] = Student(student_id, name)
        print("Student added successfully.")

    def add_exam(self):
        exam_code = input("Enter exam code: ")
        subject = input("Enter subject: ")
        self.exams[exam_code] = Exam(exam_code, subject)
        print("Exam added successfully.")

    def submit_marks(self):
        student_id = input("Enter student ID: ")
        exam_code = input("Enter exam code: ")
        if student_id in self.students and exam_code in self.exams:
            marks = float(input("Enter marks: "))
            self.students[student_id].add_marks(exam_code, marks)
            print("Marks submitted successfully.")
        else:
            print("Invalid student ID or exam code.")

    def view_report(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            print(f"\nReport for {student.name} (ID: {student.id})")
            for exam_code, marks in student.marks.items():
                exam = self.exams.get(exam_code)
                subject = exam.subject if exam else "Unknown"
                print(f"{subject} ({exam_code}): {marks}")
        else:
            print("Student not found.")
