class Animal(object):
    def __init__(self, name):
        self.name = name

    def get_sound(self):
        return "nothing."

    def make_sound(self):
        print(f"{self.name} says: {self.get_sound()}")

# overriding all methods
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name + ' the Loyal')

    def get_sound(self):
        return "Bork!"

    def make_sound(self):
        super().make_sound()
        print("He must have seen something.")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name + ' the Traitor')

    def get_sound(self):
        return "Gnaa!"
    
    def make_sound(self):
        super().make_sound()
        print(f"Then he goes back to sleep.")


class Owner:
    def __init__(self, *pets):
        self.pets = pets
        print(type(self.pets))

    def print_pets(self):
        print("These are the owned pets:")
        for p in self.pets:  
            print(f"- the owner owns {p.name}")

def main():
    c = Cat("Smith")
    d = Dog("Pollock")
    bob = Owner(c,d)
    bob.print_pets()
    

if __name__ == '__main__':
    main()