'''
Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

'''
'''
myList = ['abc', 'xyz', 'aba', '1221']
count = 0


for i in myList:
    if(len(i) >= 2 and i[0] == i[-1]):
        count += 1

print(f"count = {count}")
'''

'''
### Scenario:
You are a teacher managing a class of students. You need to keep track of the students' grades for various assignments, calculate average grades, and determine the highest and lowest grades for each assignment.

### Problem Statement:
Write a Python program to help the teacher manage the students' grades. The program should include the following functionalities:

1. Storing Grades: Use lists to store the grades of students for multiple assignments. Each assignment should have its own list of grades.

2. Calculating Averages: Calculate the average grade for each assignment.

3. Finding Extremes: Determine the highest and lowest grades for each assignment.

4. Adding Grades: Allow the teacher to add a new grade to a specific assignment.

5. Removing Grades: Allow the teacher to remove a grade from a specific assignment.

6. Updating Grades: Allow the teacher to update a grade for a specific student and assignment.

### Example:
Consider a class with the following grades for three assignments:

- Assignment 1: [85, 92, 78, 90, 88]
- Assignment 2: [79, 85, 88, 92, 75]
- Assignment 3: [90, 91, 85, 87, 93]

Your program should be able to:
1. Calculate the average grade for each assignment.
2. Find the highest and lowest grades for each assignment.
3. Add a new grade to an assignment, for example, adding 95 to Assignment 1.
4. Remove a grade from an assignment, for example, removing 78 from Assignment 1.
5. Update a grade for a student, for example, changing the second student's grade from 85 to 89 in Assignment 1.

'''

assignment_1 = [85, 92, 78, 90, 88]
assignment_2 = [79, 85, 88, 92, 75]
assignment_3 = [90, 91, 85, 87, 93]
choice = 0
print(assignment_1, assignment_2, assignment_3, sep="\n")

while(choice != 7):
    print("1. Storing Grades\n2. Calculate Averages\n3. Finding Extremes\n5. Removing Grades\n6. Updating Grades\n7. Exit")

    choice = int(input("Enter your choice: "))

    if(choice == 1):
        print("1. Assignment 1\n2. Assignment 2\n3. Assignment 3\n4. Exit")
        choice = int(input("Enter the assignment number: "))

        if(choice == 1):
            n = int(input("Enter how many grades you want to enter(>0): "))
            if (n > 0 and n == 1):
                assignment_1.append(int(input("Enter Grade: ")))
            elif (n > 0):
                newList = []
                for i in range(n):
                    newList.append(int(input(f"Enter Grade {i}: ")))
                assignment_1.extend(newList)
            break   # end of ass_1

        elif (choice == 2):
            n = int(input("Enter how many grades you want to enter(>0): "))
            if (n > 0 and n == 1):
                assignment_2.append(int(input("Enter Grade: ")))
            elif (n > 0):
                newList = []
                for i in range(n):
                    newList.append(int(input(f"Enter Grade {i}: ")))
                assignment_2.extend(newList)
            break   # end of ass_2

        elif (choice == 3):
            n = int(input("Enter how many grades you want to enter(>0): "))
            if (n > 0 and n == 1):
                assignment_3.append(int(input("Enter Grade: ")))
            elif (n > 0):
                newList = []
                for i in range(n):
                    newList.append(int(input(f"Enter Grade {i}: ")))
                assignment_3.extend(newList)
            break   # end of ass_3
        
        else:
            print("Exiting Storing Grades Menu")
            break   # end of exit
        
        # break   # end of storing grades
    else:
        pass

print(assignment_1, assignment_2, assignment_3, sep="\n")