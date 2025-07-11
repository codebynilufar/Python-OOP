class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade
    def get_info(self) -> str:
        return f"{student.name}, {student.age}-yoshda, {student.grade} o'quvchisi. "
    
student = Student("Ali", 15, "9-sinf")

print(student.get_info())