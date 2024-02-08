# Correct each program

# Program 1
def greet(name = input("Please enter your name: ")):
    print("Hello, " + name + "!")
greet()

# Program 2
x = 5
y = 10
result = str(int(x) + int(y))
print("Result: " + result)

# Program 3
def calculate_area():
    circumference = input("Please enter the circumference of your circle: ")
    radius = int((int(circumference) / 6.28318530718))
    area = str((int(radius) ** 2) * 3.14)
    print("Area Of Circle = " + area)
calculate_area()

# Program 4
number = int(input("Enter a number: "))
if (number % 2)  == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Program 5
def add_numbers(a, b):
    return a + b 
add_numbers()

# Program 6
def print_message():
    print("This message will apper now")
print_message()

# Program 7
numbers = [1, 2, 3, 4, 5]
sum = int(int(1) + int(2) + int(3) + int(4) + int(5))
len = int(5)
average = str(int(sum) / int(len))
print("Average: " + average)

# Program 8
for i in range(1, 6):
    print(i)

# Program 9
def multiply():
    a = int(5)
    b = int(10)
    result = str(int(a) * int(b))
    return result
print(multiply())

# Program 10
def check_temperature():
    temp = input("What's the tempretature?: ")

    if temp > "30":
        print("It's hot outside.")
        
    else:
        print("It's cool outside.")
check_temperature()
