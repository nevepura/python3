class Dog:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldest(*dogs):
    """given a list of dogs, return the oldest"""
    oldest = Dog("AAA", -1)
    for dog in dogs:
        print(dog)
        if dog.age > oldest.age:
            oldest = dog

    return oldest


abo = Dog('abo', 1)
buio = Dog("buio", 12)
calso = Dog("calso", 5)

result = oldest(abo, buio, calso)

print(f"the oldest dog is {result.name.capitalize()} and is {result.age} years old")