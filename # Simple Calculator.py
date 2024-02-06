# Simple Calculator

print("Please select an option: ")
print("1. Add") 
print("2. Substract") 
print("3. Multiply") 
print("4. Divide") 

operation = input()

if operation == 1:
    number1 = input("Please enter your first number: ")
    number2 = input("Please enter your second number: ")
    print("Adding these numbers together give you: " + number1 + number2)
elif operation == 2:
    number1 = input("Please enter your first number: ")
    number2 = input("Please enter your second number: ")
    print("Subtracting these numbers together give you: " + number1 - number2)
elif operation == 3:
    number1 = input("Please enter your first number: ")
    number2 = input("Please enter your second number: ")
    print("Adding these numbers together give you: " + number1 + number2)
elif operation == 4:
    number1 = input("Please enter your first number: ")
    number2 = input("Please enter your second number: ")
    print("Adding these numbers together give you: " + number1 + number2)
else:
    print("Please put a valid number")
    