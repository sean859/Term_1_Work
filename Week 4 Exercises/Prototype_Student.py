import copy
from Prototype_Person import Person
from Prototype_Teacher import Teacher

# ConcreatePrototype2
class Student(Person):
    def __init__(self, name: str, teacher: Teacher):
        super().__init__(name)
        self.teacher = teacher

    def clone(self):
        return copy.copy(self) # Or instead of copy.copy(self), you have copy.deepcopy(sefl) so that when the teacheg 'get_course' is moditify its dosen't change the display text for the 'studentclone' 
    
    def display(self):
        print('Student was cloned:')
        print('-------------------')
        print(f'Student Name: {self.name}')
        print(f'Is Learning: {self.teacher.get_course()}')
        print(f'Taught By: {self.teacher.get_name()}\n')