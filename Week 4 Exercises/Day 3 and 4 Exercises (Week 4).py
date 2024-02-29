# Pattern Designs

# Creational Design Pattern

# Factory Method:
# The Factory Method also known as a Virtual Constructor, is a creational pattern design that provides an interface for creating objects in a parent class (superclass), then allows creation for child classes
# (subclasses) to alter the type of objects that will be created, using this method will allow the bulk of the code to be in a single superclass then when changes need to made to fit something else it can be
# inherited to a subclass that fits the more specific needs for that objects, example you have sea, land, and air vechiles, they can all fall under transport but different kinds of transport so, 'Transport' can
# be your superclass well 'Air Transport', 'Sea Transport', and 'Land Transport' can be your subclasses to fit inheriet from 'Transport' but still cater to the different requirments for the objects well also
# returning there respective object type (Plane, Sea, Land).

# Code
class PresidentOffice:
    _instance = None
    _president = None
 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PresidentOffice, cls).__new__(cls)
            cls._president = "John Doe"  # Assign the President
        return cls._instance
 
    def meet_president(self, visitor_name):
        print(f"{visitor_name} is meeting President {self._president}")
 
# Usage
office1 = PresidentOffice()
office2 = PresidentOffice()
 
office1.meet_president("Alice")  # Alice is meeting President John Doe
office2.meet_president("Bob")    # Bob is meeting President John Doe
 
print(office1 is office2)  # True, both variables reference the same instance


# Prototype:
# The prototype method is a creational design pattern that specifies the kind of objects to create using a prototypical instance and creates new objects by copying this prototype making either a shadow copy that can
# only copy primitive types and another one called deep copy that can also create refrence types.

# Code
from Prototype_Teacher import Teacher
from Prototype_Student import Student

# Client
def main():
    teacher = Teacher("Random Name", "Software Development")            
    teacherclone = teacher.clone()
    teacherclone.display()

    student = Student("Another Random Name", teacherclone)
    studentclone = student.clone()
    studentclone.display()  

    # Modify Teacher Clone
    teacherclone.set_course("Not Software Development")
    studentclone.display()

if __name__ == "__main__":
    main()

# Copy = Shadow copy meaning that if the refrence to an object is changed, all clones will inherit that change
    
# Deepcopy = Deep copy meaning that if the refrence to an object is changed, all clones will not change

# Singleton




