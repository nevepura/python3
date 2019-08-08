import numpy as np

a = ([[1,2,3]])
b = ([[4,5,6]])
c = np.array([
	[1,2,3],
	[4,5,6]
	])

d = np.array([
	[0,1,1],
	[0,1,2]
	])


#print(np.dot(a,b))
print(np.dot(c,d.T))
print(np.multiply(c,d))