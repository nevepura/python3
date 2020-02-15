class Fish:
    def __init__(self, name, surname, skeleton="bones", eyelids=False):
        self.name = name
        self.surname = surname
        self.skeleton = skeleton
        self.eyelids = eyelids
    
    def swim(self):
        print("This fish can swim.")
    
    def swim_backwards(self):
        print("This fish can swim backwards.")


class Trout(Fish):
    def __init__(self, water="fresh water"):
        self.water = water
        super().__init__('nome', 'cognome')

'''
a = Fish("Mario",'Rossi')
print(f'{a.name}, {a.surname}, {a.skeleton}, {a.eyelids}')
'''


b = Trout()

print(f'{b.name}, {b.surname}, {b.skeleton}, {b.eyelids}')
