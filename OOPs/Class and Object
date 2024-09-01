class Student:
    # attributes
    rollNo = None
    name = None
    grade = None


    # methods - instance methods
    def scanStudent(self, rno: int, n: str, grd: int) -> None:
        self.rollNo = rno
        self.name = n
        self.grade = grd

    def printStudentDetails(self):
        print(f"\nRollNo: {self.rollNo}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")

"""
s = Student()   # object

# s.rollNo = 101
# s.name = "Dhairya"
# s.grade = 8

# calling method
s.scanStudent(101, "Dhairya", 8)
# s.marks = 67    # adding attribute directly

# print(f"RollNo: {s.rollNo}")
# print(f"Name: {s.name}")
# print(f"Grade: {s.grade}")
# print(f"Marks: {s.marks}")

s.printStudentDetails()

s1 = Student()
# s1.scanStudent(102, "Krish", 7)
s1.printStudentDetails()
"""

s: object   # object
s = Student()   # instance

s.scanStudent(102, "Mithil", 4)
s.marks = 32+1  # created a new attribute specifically for s(current) instance

s.printStudentDetails()
print(f"Marks: {s.marks}")

s1 = Student()

s1.printStudentDetails()
print(f"Marks: {s1.marks}")