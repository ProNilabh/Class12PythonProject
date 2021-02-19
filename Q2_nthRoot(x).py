#Write a function namely nthRoot() that receives two parameters x and n and returns nth root of x

def NthRoot(x,n):
    x=x**(1/n)
    return x

x=int(input("Enter a Number:") )
n=int(input("Enter Root Value:"))

print("The", n, "ᵗʰ Root of", x, "is", NthRoot(x,n))

print("Thanks for Using the Program!")