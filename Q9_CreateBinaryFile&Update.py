#Create a binary file with roll number, name and marks. Input a roll number and update the marks

import pickle

student = []

file = open('student.dat', 'wb')
ans = 'yes'

while ans.lower()=='yes':
    roll = int(input("Enter Roll Number:"))
    name = input("Enter Name:")
    marks = int(input("Enter Marks:"))
    student.append([roll, name, marks])
    ans = input("Do you want to Add More Records? (ENTER yes):")

pickle.dump(student, file)
file.close()

file = open('student.dat', 'rb+')

student = []

while True:
    try:
        student = pickle.load(file)
    except EOFError:
        break

ans = 'yes'

while ans.lower()=='yes':
    found = False
    roll_update = int(input("Enter the Roll Number to Update:"))
    for s in student:
        if s[0]==roll_update:
            print("Name is:", s[1])
            print("Current Marks is:", s[2])
            new_marks = int(input("Enter New Marks:"))
            s[2] = new_marks
            print("Record Updated")
            found = True
            break
    if not found:
        print("Sorry! Roll Number Not Found")
    ans = input("Want to Update More Marks? (ENTER yes):")

file.close()

print("Thanks for Using the Program!")