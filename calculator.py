#add subtract multiply divide 


def add_numbers(num1, num2):
    print (num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)


def multiply(num1, num2):
    print(num1 * num2)
    
def divide(num1, num2):
    print(num1/num2)


#main
def calculator():
    #running = True
    print("Welcome to my calculator. select 1(add), 2(subtract), 3(multiply), 4(divide)")
    
    choice = int(input("Please choose a number to peform an operation: "))
    
    
    if choice == 1:
        add_numbers(num1, num2)
    elif choice == 2:
            subtract(num1, num2)
    elif choice ==3: 
            multiply(num1, num2)
    elif choice == 4:
        divide(num1, num2)
        running = False
    else:
        print("Invalid Option ): ")

num1 = int(input("Please input the first number: "))
num2 = int(input("Please input the second number: "))

calculator()
