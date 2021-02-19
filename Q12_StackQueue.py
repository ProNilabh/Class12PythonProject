#Python Program to Implement a Stack and Queue using a List Data-Structure

top = None

def isEmpty(stk): # Checks whether the Stack is Empty or Not
   if stk==[]:
      return True
   else:
      return False

def Push(stk,item): # Allow additions to the Stack
   stk.append(item)
   top = len(stk)-1

def Pop(stk):
   if isEmpty(stk): # Verifies whether the Stack is empty or not
      return("UnderFlow")
   else: # Allow deletions from the stack
      item = stk.pop()
      if len(stk)==0:
         top = None
      else:
         top=len(stk)
         print("Popped item is "+str(item))

def Peak(stk):
   if(isEmpty(stk)):
      return("UnderFlow")
   else:
      top = len(stk) - 1
      return stk[top]

def Display(stk):
   if isEmpty(stk):
      print("Stack is empty")
   else:
      top=len(stk)-1
      print("Elements in the stack are: ")
      for i in range(top,-1,-1):
         print (str(stk[i]))

if __name__ == "__main__":
   stk=[]

while True:
   print("STACK IMPLEMENTATION")
   print("1. PUSH")
   print("2. POP")
   print("3. PEEK")
   print("4. DISPLAY")
   print("5. EXIT")
    
   ch = int(input("Enter a No.:"))

   if ch==1:
      item = int(input("Enter the Item you want to PUSH:"))
      Push(stk,item)
      print("%d Added Sucessfully"%item)
      input("Press any key to Continue...")

   elif ch==2:
      item = Pop(stk)
      if (item == "UnderFlow"):
         print("UnderFlow! Stack is EMPTY!")
      else:
         input("Press any key to Continue...")

   elif ch==3:
      item = Peak(stk)
      if (item == "UnderFlow"):
         print("UnderFlow! Stack is EMPTY!")
      else: 
         print("%d"%item)
      input("Press any key to Continue...")

   elif ch==4:
      Display(stk)
      input("Press any key to Continue...")

   elif ch==5:
      print("Thanks for using, Give your Valuable Feedback")
      print("DESINED BY Nilabh Pandey® | E-Mail: nilabhpandey7@gmail.com | ©️ ProNilabh2K21")
      break

   else:
      print("Enter A Correct No.")
      input("Press any key to Continue...")