class School:
    def __init__(self, name: str, grade: int) -> None:
        self.name = name
        self.grade = grade

    def displaySchoolDetails(self) -> None:
        print(f"School Name: {self.name}")
        print(f"Grade: {self.grade}")

class Student (School): # student class gets inherited by school class
    
    def __init__(self, schoolName: str, grade: int, name: str, rollno: int, marks: int, fees: float) -> None:
        super().__init__(schoolName, grade)   # calling parent class' constructor
        self.name = name
        self.rollno = rollno
        self.marks = marks
        self.fees = fees

    def displayStudentDetails(self) -> None:
        print(f"Student Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Marks: {self.marks}")
        print(f"Fees: {self.fees}")

    def showDetails(self):
        print("School Details: ")
        self.displaySchoolDetails()
        
        print("\nStudent Details: ")
        self.displayStudentDetails()


if __name__ == "__main__":
    # s1 = School("School of Achiever", 11)
    s = Student("School of Achiever", 11, "Arin P.", 462, 40, 100000)

    # s1.displaySchoolDetails()
    s.showDetails()
