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
            if input() == "Yes":
                  Contact_Book[self.name] = "Phone: " + self.phone, "Email: " + self.email
                  print("Your record has been added")
                  print(Contact_Book)
            else:
                 print("New Record Addition Cancelled") 

# Where as this class will be used for the Add Extra Vendor Details so that it has the compulsory info including some extra information
class ExtraVender(Vender):
     def __init__(self, name, phone, email, company, parentalcontact, medical):
          super().__init__(name, phone, email)
          self.company = company
          self.parentalcontact = parentalcontact
          self.medical = medical
     def print_extra_vender(self):
            print("Are These details correct?")
            print("Name: " + self.name)
            print("Phone: " + self.phone)
            print("Email: " + self.email)
            print("Company: " + self.company)
            print("Parent Contact: " + self.parentalcontact)
            print("Medical Condition: " + self.medical)
            print("If correct type 'Yes', otherwise type nothing")
            if input() == "Yes":
                  Contact_Book[self.name] = "Phone: " + self.phone, "Email: " + self.email, "Company: " + self.company, "Parent Contact: " + self.parentalcontact, "Medical Condition: " + self.medical
                  print("Your record has been added")
                  print(Contact_Book)
            else:
                 print("New Record Addition Cancelled")
     
            
# Contact Book Global Functions 
# The point of these functions to be used throughout the 
# code allowing less strain on the code and more tidyness

# This function is the main menu where all the functions below will be accessed depending on the users input
def ContactBook():
    print("-----Contact Book-----")
    print("To select an option press the corrosponding number")
    print("1. Add New Vender")
    print("2. Add New Vender (With Addition Information)")
    print("3. Access Vender Information")
    print("4. Remove Current Vender Information")
    print("5. Update Current Vender Information")

    contactbookinput = input()

    if contactbookinput == "1":
        Add_New_Vender()
    elif contactbookinput == "2":
        Add_Extra_Vender_Info()
    elif contactbookinput == "3":
        Access_Vender_Info()
    elif contactbookinput == "4":
        Remove_Vender()
    elif contactbookinput == "5":
        Update_Vender()
    else:
        print("Please enter a valid number")
        ContactBook()

# This Function will allow new venders to be added with their info
def Add_New_Vender():
    print("Please enter your full name")
    name = input()
    print("Please enter your phone number")
    phone = input()
    print("Please enter your email address")
    email = input()
    NewVender = Vender(name, phone, email)
    NewVender.print_vender() 
    ContactBook() 

# This function will allow vendors to add extra info they want to provide if the compulsory info isn't enough
def Add_Extra_Vender_Info():
    print("Please enter your full name")
    name = input()
    print("Please enter your phone number")
    phone = input()
    print("Please enter your email address")
    email = input()
    print("Please enter your company name")
    company = input()
    print("Please enter your parental contact number")
    parentalcontact = input()
    print("Please enter your medical condition")
    medical = input()
    ExtraVender_2 = ExtraVender(name, phone, email, company, parentalcontact, medical)
    ExtraVender_2.print_extra_vender()
    ContactBook()

# This function will allow "Stellar Events" to access the info the vender via searching by their full name
def Access_Vender_Info():
    print("Search by full name")
    search = input()
    if search in Contact_Book:
         print(Contact_Book.get(search))
         ContactBook()
    else:
         print("No Record Found")
         ContactBook()

# This function will allow "Stellar Events" to remove any vender and all their info 
def Remove_Vender():
    removethisperson = input("Type the full name of the record you want to delete: ")
    if removethisperson in Contact_Book:
        Contact_Book.pop(removethisperson)
        print(removethisperson + " was removed from record")
        ContactBook()
    else:
         print("Record Not Found")
         ContactBook()

# This function will allow venders to update their info so that its more relevant
def Update_Vender():
    updateoldvender = input("Please type the full name of the vender you want to update: ")
    if updateoldvender in Contact_Book:
         Contact_Book.pop(updateoldvender)
         print("Updating " + updateoldvender)
         Add_New_Vender()
         print(updateoldvender + " has been updated")
         ContactBook()
    else:
         print("That Record Does Not Exist")
         ContactBook()

ContactBook()
