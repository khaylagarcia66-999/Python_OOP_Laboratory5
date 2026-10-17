class Student:
    def __init__(self, grade):
        self.__grade = grade  # Encapsulation

    def study(self):  # Abstraction
        print("Student is studying.")


class CollegeStudent(Student):  # Inheritance
    def study(self):  # Polymorphism
        print("College student is studying programming.")


student = Student(90)
college = CollegeStudent(95)

student.study()
college.study()