'''
special methods seen are: init, str, len, bool
note: if boof and len are not defined, bool(obj) returns true
'''

class Person:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname

	def __str__(self):
		return '{} {}'.format(self.name, self.surname)
	def __repr__(self):
		return '<Person object (name = {}, surname = {})>'.format(self.name, self.surname)

	def __len__(self):
		return(len(self.name)+len(self.surname))
	def __bool__(self):
		return(len(self)>=4)

class Bomber:
	pass

p = Person('Gianni','Rodari')
f = Person('o','aa')
'''
print(p)
print(str(p))
print(repr(p))
'''
#b = Bomber()
#print(repr(b))

print(len(p))
print(bool(f))