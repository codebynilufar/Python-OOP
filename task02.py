class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade

student = Student("Nilufar", 19, "A")
print(f"Name :{student.name}")
print(f"Age: {student.age}")
print(f"Grade{student.grade}")
     