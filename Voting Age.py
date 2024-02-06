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