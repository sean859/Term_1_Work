# Contact Book Application
Contact_Book ={}

# Contact Book Classes

# This class will be used to store the objects used for compoulsory info
class Vender:
        def __init__(self, name, phone, email):
            self.name = name
            self.phone = phone
            self.email = email
        def print_vender(self):
             print("Are These details correct?")
             print("Name: " + self.name)
             print("Phone: " + self.phone)
             print("Email: " + self.email)
             print("If correct type 'Yes', otherwise type nothing")


# Contact Book Global Functions 
# The point of these functions to be used throughout the 
# code allowing less strain on the code and more tidyness

# This Function will allow new venders to be added with their info
def Add_New_Vender():
    print("Please enter your full name")
    name = input()
    print("Please enter your phone number")
    phone = input()
    print("Please enter your email address")
    email = input()
    new_vender = Vender(name, phone, email)
    new_vender.print_vender()
    if input() == "Yes":
         Contact_Book[name] = 'Phone:', phone, 'Email:', email
         print("Your details have been added to the contact book")
    else:
         print("Then please try again")
         Add_New_Vender()
Add_New_Vender()

# This function will allow "Stellar Events" to access the info the vender via searching by their name
def Access_Vender_Info():
    pass


# This function will allow "Stellar Events" to remove any vender and all their info 
def Remove_Vender():
    pass

# This function will allow venders to update their info so that its more relevant
def Update_Vender():
    pass

# This function will allow vendors to add extra info they want to provide if the compulsory info isn't enough
def Add_Extra_Vender_Info():
    pass

