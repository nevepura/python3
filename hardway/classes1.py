class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

d1 = Dog('Garurumon', '1')
print(d1.name + ' ' + d1.age)

d2 = Dog('pipo', 0xacd)
print('name = {}, age = {}'.format(d2.name, d2.age))
