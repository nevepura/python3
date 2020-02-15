class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def print_name(self):
        print(self.firstname, self.lastname)
    

class Student(Person):
    def __init__(self, first, last, age=0):
        # Person.__init__(self, first, last)
        # super(Student, self).__init__(first,last) # MOST RELIABLE WAY TO CALL SUPER()
        # print(super())
        super().__init__(first, last)
        self.age = age
    


ennio = Person("Ennio", "Morricone")
ennio.print_name()

'''
alfio = Student("Alfio", "Rotoverto", 26)
alfio.print_name()
print(alfio.age)
'''