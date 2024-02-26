# Simple Calculator

def simple_calculator():
    print("Please select an option: ")
    print("1. Add") 
    print("2. Substract") 
    print("3. Multiply") 
    print("4. Divide") 

    operation = input()

    if operation == "1":
        number1 = input("Please enter your first number: ")
        number2 = input("Please enter your second number: ")
        print("Adding these numbers together give you: " + str(int(number1) + int(number2)))
    elif operation == "2":
        number1 = input("Please enter your first number: ")
        number2 = input("Please enter your second number: ")
        print("Subtract these numbers together give you: " + str(int(number1) - int(number2)))
    elif operation == "3":
        number1 = input("Please enter your first number: ")
        number2 = input("Please enter your second number: ")
        print("Multiply these numbers together give you: " + str(int(number1) * int(number2)))
    elif operation == "4":  
        number1 = input("Please enter your first number: ")
        number2 = input("Please enter your second number: ")
        print("Dividing these numbers together give you: " + str(int(number1) / int(number2)))
    else:
        print("Please put a valid number")
simple_calculator()
# Voting Age Verifier
def voter_eligibility(age):
    return age >= 18

def main():
    try:
        age = int(input("Input your age: "))
        
        if age < 0:
            print("Age cannot be negative.")
        elif voter_eligibility(age):
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please input a valid age.")
main()

# Check If Number Is Even Or Odd

def EvenOrOdd():
    number = int(input("Please enter a number: "))
    
    if (number % 2) == 0:
        print("You have typed an even number")
    else:
        print("You have typed an odd number")
EvenOrOdd()



