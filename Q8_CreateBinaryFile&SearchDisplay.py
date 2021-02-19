#Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message

import pickle

student = []

file = open('student.dat', 'wb')
ans = 'yes'

while ans.lower()=='yes':
    roll = int(input("Enter Roll Number:"))
    name = input("Enter Name:")
    student.append([roll, name])
    ans = input("Do you want to Add More Records? (ENTER yes):")

pickle.dump(student, file)
file.close()

file = open('student.dat', 'rb')
student = []

while True:
    try:
        student = pickle.load(file)
    except EOFError:
        break

ans = 'yes'

while ans.lower()=='yes':
    found = False
    k = int(input("Enter Roll Number to Search:"))
    for s in student:
        if s[0]==k:
            print("Name is:", s[1])
            found = True
            break
    if not found:
        print("Sorry! Roll Number not Found")
    ans = input("Do You want to Search More? (ENTER yes):")

file.close()

print("Thanks for Using the Program!")