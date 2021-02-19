#Read a Text File and Display the Number of Vowels/Consonants/Uppercase/Lowercase Characters in the File

file = input("Enter the file to check: ").strip()

infile = open(file, 'r')

vowels = set("A E I O U a e i o u")
cons = set("b c d f g h j k l m n p q r s t v w x y z B C D F G H J K L M N P Q R S T V W X Y Z")

text = infile.read().split()

countV = 0
countC = 0
upper=0
lower=0

for V in text:
    if V in vowels:
        countV += 1

for C in text:
    if C in cons:
        countC += 1

for i in range(len(text)):
    if(str[i]>='a' and str[i]<='z'):
        lower+=1
    elif(str[i]>='A' and str[i]<='Z'):
        upper+=1

print("The Number of Vowels is: ",countV)
print("The Number of consonants is: ",countC)
print("The Number of Uppercase Letters: ",upper)
print("The Number of Lowercase Letters: ",lower)

print("Thanks for Using the Program!")