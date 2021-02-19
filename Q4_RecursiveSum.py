# Write a Recursive Code to find the Sum of all Elements of a List

def FindSum(list1): 
     if len(list1)== 1: 
        return list1[0] 
     else: 
        return list1[0]+FindSum(list1[1:])

# Input Values to List

list1 = list(input("Enter the List:"))

print(FindSum(list1))