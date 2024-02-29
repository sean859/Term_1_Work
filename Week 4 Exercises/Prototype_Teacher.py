import copy
from Prototype_Person import Person

# ConcretePrototype1
class Teacher(Person):
    def __init__(self, name: str, course: str):
        super().__init__(name)
        self.course = course
    
    def clone(self):
        return copy.copy(self)
    
    def display(self):
        print('Teacher was cloned:')
        print('-------------------')
        print(f'Name: {self.name}')
        print(f'Who Teaches: {self.course}\n')
    
    def get_course(self):
        return self.course
    
    def set_course(self, course: str):
        self.course = course