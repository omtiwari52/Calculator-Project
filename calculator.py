def add (x,y):
    return x+y

def subtract(x,y):
    return x-y

def divide (x,y):
    return x / y 

def multiply (x,y):
    return x*y

print("select operation : ")
print("1.Add")
print("2.Substract")
print("3.Divide")
print("4.Multiply")

while True:
    
    choice = input("enter choice \n (1\t2\t3\t4) : ")

    if choice in ('1','2','3','4'):
        num1 = int(input("enter first number : "))
        num2 = int(input("Enter second number : "))

        if choice == '1':
            print(num1 , "+" , num2 , "=" , add(num1,num2))

        elif choice == '2':
            print(num1 , "-" , num2 , "=" , subtract(num1,num2))

        elif choice == '3':
            print(num1 , "/" , num2 , '=' , divide(num1,num2))

        elif choice == '4':
            print(num1 , "*" , num2 , "=" , multiply(num1,num2))

        next_calculation = input("let's do next calculation..?? \n 1.Yes \n 2.No \n")
        if next_calculation == "No":
            break
        else :
            print("Invalid Request")