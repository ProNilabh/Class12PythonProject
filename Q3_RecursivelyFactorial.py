# Recursively find the Factorial of a Natural Number

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)


x = int(input("Enter the No.:"))

# Check if the Number is Negative

if x < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif x == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", x, "is", recur_factorial(x))