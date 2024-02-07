# User Input

# Input Prompt:
username = input("Please type your name: ")
print("Good day to you " + username + " hows it going?")

# Nummeric Input:
number1 = input("Please enter your first number: ")
number2 = input("Please enter your second number: ")
print("Adding these numbers together give you: " + str(int(number1) + int(number2)))

# Favourite Color:
favcolor = input("Do you think you can tell us your favourite color " + username + ": ")
print("Wow, " + favcolor + " isn't a bad color but my personal favourite is Gamboge")

# Output

# Print Multiple Lines:
print("Hey wanna see something cool?")
print("Type Yes")
print("Type No")

somethingcool = input()

if somethingcool == "Yes":
    print("Look at this cool message")
    print("And this one")
    print("Can't forget about this one")
    print("And last but not least this one")
elif somethingcool == "No":
    print("Oh ok")
    print("You sure though I mean like it would've been cool")
    print("But your choice at the end of the day")
    print("Just wanted to do something cool")
else:
    print("Wait where did you get this response from?")
    print("Wasen't from me")
    print("Well I guess theres so many other words out their apart from Yes or No")
    print("But this example those two would have been nice but I guess this also works")

# Formatted Output:
print("Well " + username + " Im quite shocked you like the color " + favcolor + " but you do you")

# Repeated Output: 
for Hello in range(0, 5):
    print("Hello")

# Variables
    
# Variable Swap:
firstvariable = input("Please input a value: ")
secondvariable = input("Please input another value: ")
print("First Variable = " + firstvariable)
print("Second Variable = " + secondvariable)
placeholder = firstvariable
firstvariable = secondvariable
secondvariable = placeholder
print("Your first variable is now " + firstvariable)
print("And your second variable is now " + secondvariable)

# Variable Concatenation: 

