def Input_Prompt():
        username = input("Please type your name: ")
        print("Good day to you " + username + " hows it going?")
        return username
Input_Prompt()
def Favourite_Color():
        favcolor = input("Do you think you can tell us your favourite color " + Input_Prompt() + ": ")
        print("Wow, " + favcolor + " isn't a bad color but my personal favourite is Gamboge")
        return favcolor
Favourite_Color()

def User_Input():

    # Input Prompt:
    def Input_Prompt():
        username = input("Please type your name: ")
        print("Good day to you " + username + " hows it going?")
        return username
    Input_Prompt()

    # Nummeric Input:
    def Nummeric_Input():
        number1 = input("Please enter your first number: ")
        number2 = input("Please enter your second number: ")
        print("Adding these numbers together give you: " + str(int(number1) + int(number2)))
    Nummeric_Input()

    # Favourite Color:
    def Favourite_Color():
        favcolor = input("Do you think you can tell us your favourite color " + Input_Prompt() + ": ")
        print("Wow, " + favcolor + " isn't a bad color but my personal favourite is Gamboge")
        return favcolor
    Favourite_Color()

def Output():

    # Print Multiple Lines:
    def Print_Multiple_Lines():
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
    Print_Multiple_Lines()

    # Formatted Output:
    def Formatted_Output():
        print("Well " + Input_Prompt() + " Im quite shocked you like the color " + Favourite_Color() + " but you do you")
    Formatted_Output()

    # Repeated Output: 
    def Repeated_Output():
        for Hello in range(0, 5):
            print("Hello")
    Repeated_Output()

def Variables():
    
    # Variable Swap:
    def Variable_Swap():
        firstvariable = input("Please input a value: ")
        secondvariable = input("Please input another value: ")
        print("First Variable = " + firstvariable)
        print("Second Variable = " + secondvariable)
        placeholder = firstvariable
        firstvariable = secondvariable
        secondvariable = placeholder
        print("Your first variable is now " + firstvariable)
        print("And your second variable is now " + secondvariable)
    Variable_Swap()

    # Variable Concatenation: 

    # Variable Initilization:
    def Variable_Initilization():
        actualage = input("Please enter your age")
        print("Your age is " + actualage)
    Variable_Initilization()

def Operators():

    # Arithmetic Operations:
    def Arithmetic_Operations():
        print("Please select an option: ")
        print("1. Add") 
        print("2. Substract") 
        print("3. Multiply") 
        print("4. Divide") 

        operation = input()

        if operation == "1":
            num1 = input("Please enter your first number: ")
            num2 = input("Please enter your second number: ")
            print("Adding these numbers together give you: " + str(int(num1) + int(num2)))
        elif operation == "2":
            num1 = input("Please enter your first number: ")
            num2 = input("Please enter your second number: ")
            print("Subtract these numbers together give you: " + str(int(num1) - int(num2)))
        elif operation == "3":
            num1 = input("Please enter your first number: ")
            num2 = input("Please enter your second number: ")
            print("Multiply these numbers together give you: " + str(int(num1) * int(num2)))
        elif operation == "4":  
            num1 = input("Please enter your first number: ")
            num2 = input("Please enter your second number: ")
            print("Dividing these numbers together give you: " + str(int(num1) / int(num2)))
        else:
            print("Please put a valid number") 
    Arithmetic_Operations()