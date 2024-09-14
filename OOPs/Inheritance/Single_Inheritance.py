class School:
    def __init__(self, name: str, grade: int) -> None:
        self._name = name
        self._grade = grade

    def displaySchoolDetails(self) -> None:
        print(f"School Name: {self._name}")
        print(f"Grade: {self._grade}")

class Student (School): # student class gets inherited by school class
    
    def __init__(self, schoolName: str, grade: int, name: str, rollno: int, marks: int, fees: float) -> None:
        School.__init__(self, schoolName, grade)   # calling parent class' constructor
        self.__name = name
        self.__rollno = rollno
        self.__marks = marks
        self.__fees = fees

    def displayStudentDetails(self) -> None:
        print(f"Student Name: {self.__name}")
        print(f"Roll No: {self.__rollno}")
        print(f"Marks: {self.__marks}")
        print(f"Fees: {self.__fees}")

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
