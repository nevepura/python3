class Test:
	classname = "Test" #attributo di istanza
	def __init__(self, nome):	
		print("chiamata a init")
		self.nome = nome # attributo di istanza
		
	def print_nome(self):
		print(self.nome)

# altering class variable 'classname'
Test.classname = "no more test"
print(Test.classname)

# creating Test objects
t1 = Test("paperolamo")
print(t1.nome)
t1.nome = "paperagno"
print(t1.nome)



