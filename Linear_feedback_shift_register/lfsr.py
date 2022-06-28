'''
Linear Feedback Shift Register. 
Used as random generator. 
Generates all random combinations of 1 and 0 of same length of input

See: https://www.youtube.com/watch?v=Ks1pw1X22y4&t=233s
'''

start = 0b1001
print(bin(start))
print()
a = start
b = None 
prefix = '0b'
i=0

while b != start and  i < 100:
	
	i+=1
	print(f'a: {bin(a)}')

	padded = prefix + bin(a)[2:].rjust(4,'0')
	new_bit = int(padded[-1]) ^ int(padded[-2])
	shifted = bin(a >> 1)[2:].rjust(3,'0')

	b = int(prefix + str(new_bit) +  shifted, 2)
	print(f'b: {bin(b)}\n')
	a = b

# Should complete in 2^(len(input) -1 ) iterations
print(f'Completed in {i} iterations.')
