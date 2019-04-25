class Drone:
	def __init__(self, state, battery):
		self.state = False
		self.battery = 100
		self.position = [0,0]
	def move(self, target):
		self.position = target
		self.battery -= 1