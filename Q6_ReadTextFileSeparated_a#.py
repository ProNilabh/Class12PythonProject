#Read a text file line by line and display each word separated by a #

file = input("Enter the File Name:") 
f = open( file,'r') 

item = [] 

for line in f:
    words=line.split()
    for i in words:
        item.append(i)
        
print("#".join(item))

print("Thanks for Using the Program!")