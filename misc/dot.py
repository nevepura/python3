import numpy as np

x1 = np.array([[1,2,3]])
x2 = np.array([[2,3,0]])
x2t = x2.T

'''
print('x2: ' + str(x2))
print('x2 shape: ' + str(x2.shape))
print('x2t: ' + str(x2t))
print('x2t shape: ' + str(x2t.shape))
'''
# np.dot(x1,x2t) # PROTOTTO TRA VETTORI-MATRICE, MA ERRORE! sulle dimensioni
print('dot(x1,x2t)' + str(np.dot(x1,x2t)))

a1 = ([1,2,3])
a2 = ([0,0,1])

print('dot(a1,a2): ' + str(np.dot(a1,a2)))


m1 = np.array([
	[1,2,3],
	[4,5,6]
	])

m2 = np.array([
	[1,2,3]
	])

print('m1 shape '+ str(m1.shape))
print('m2.shape ' + str(m2.shape))

m2t = m2.T

# PRODOTTO TRA MATRICI
M = np.dot(m1,m2t)
print(M)

print(M/2)


'''
dot = np.dot(x1,x2)
print(dot)

dot2 = np.dot(x1,x2t)
print(dot2)


x3 = np.array([1,2,3])
x3b = np.array([[1,2,3]])

#print('x3: ' + str(x3))
#print('x3b: ' + str(x3b))
print(x3.shape)
print(x3b.shape)
'''