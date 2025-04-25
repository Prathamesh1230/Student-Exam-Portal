class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.marks = {}

    def add_marks(self, exam_code, marks):
        self.marks[exam_code] = marks
