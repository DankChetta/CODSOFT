def show():
    print("-----SIMPLE CALCULATOR-----")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a/b

while True:
    show()
    choice=int(input("Enter your choice (1-5):"))
    if choice==1:
        x=int(input("Enter the first number:"))
        y=int(input("Enter the second number:"))
        print("The Sum is:",add(x,y))
    elif choice==2:
        x=int(input("Enter the first number:"))
        y=int(input("Enter the second number:"))
        print("The Difference is:",sub(x,y))
    elif choice==3:
        x=int(input("Enter the first number:"))
        y=int(input("Enter the second number:"))
        print("The Product is:",mul(x,y))
    elif choice==4:
        x=int(input("Enter the first number:"))
        y=int(input("Enter the second number:"))
        print("The Quotient is:",div(x,y))
    else:
        print("Exiting Calculator")
        break