# Check If Number Is Even Or Odd

def EvenOrOdd():
    number = int(input("Please enter a number: "))
    
    if (number % 2) == 0:
        print("You have typed an even number")
    else:
        print("You have typed an odd number")

EvenOrOdd()