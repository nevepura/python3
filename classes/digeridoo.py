class Digeridoo:
	def __init__(self,length):
		print('new digeridoo created')
		self.length = length

	def play(self):
		print('Digeridoo is playing...')
		print('P'+'o'*self.length)


dig = Digeridoo(5)
dig.play()
dig2 = Digeridoo(29)
dig2.play()