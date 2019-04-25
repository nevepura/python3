class Person:
	# definiamo un __init__ che assegna nome e cognome all'istanza
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		print(name+' '+surname+' is born!')
	# definiamo un metodo "eat" che stampa un messaggio
	def eat(self, food):
		print(self.name, 'is eating', food)
	# definiamo un metodo "sleep" che stampa un messaggio
	def sleep(self):
		print(self.name, 'is sleeping')

aa = Person('Alberto','Angela')
aa.eat('history')
aa.sleep()


# Employee extends Person
class Employee(Person):
	def __init__(self, name, surname, job):
		super().__init__(name, surname)
		self.job = job
	def eat(self,food):
		print(self.name, 'is on break time:')
		super().eat(food)
	def work(self):
		print(self.name+' is working as a '+self.job)


ef = Employee('Emilio', 'Fede', 'journalist')
ef.eat('spaghetti')
ef.work()