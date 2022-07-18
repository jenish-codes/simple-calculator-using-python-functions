#Simple Calculator using python functions


from secrets import choice


def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

no1 = eval(input("Enter the first number: "))
no2 = eval(input("Enter the second number: "))

print(no1, no2)

print(""" 

Select an Option 

    [1] - Addition
    [2] - Subtraction
    [3] - Multiplication
    [4] - Division
    [5] - Exit

""")

while(True):
    choice = int(input("Enter the choice: "))
    if choice in (1,2,3,4,5):
        if choice == 1:
            print("Addition of ", no1, " and ", no2, " is: ", add(no1, no2))
        elif choice ==2:
            print("Subtraction of ", no1, " and ", no2, " is: ", subtract(no1, no2))
        elif choice ==3:
            print("Multiplication of ", no1, " and ", no2, " is: ", multiply(no1, no2))
        elif choice ==4:
            print("Division of ", no1, " and ", no2, " is: ", divide(no1, no2))
        elif choice ==5:
            print("Bye! See you soon!")
            exit()
    else:
        print("Invalid Input! Try again!")