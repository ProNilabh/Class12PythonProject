#Remove all the lines that contain the character 'a' in a file and write it to another file

file = input("Enter the File Name:")

f1=open(file,'r')
f2=open('NewFile.txt','w')

l=f1.readlines()

for i in l:
    if 'a' in i:
        i=i.replace('a','')
        f2.write(i)

f1.close()
f2.close()

print("Thanks for Using the Program!")