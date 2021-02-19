#Write a  Recursive Fibonacci(n): 

def Fibonacci(n): 
    
    if n<0: 
        print("Incorrect Input")  # First Fibonacci Number is 0 
    
    elif n==1: 
        return 0 # Second Fibonacci Number is 1 
    
    elif n==2: 
        return 1
        
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
 
x = int(input("Enter a No.:"))

print(Fibonacci(x)) # Function for nth Fibonacci Number