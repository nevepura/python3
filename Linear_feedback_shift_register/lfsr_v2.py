'''
Linear Feedback Shift Register. 
Used as random generator. 
Generates all random combinations of 1 and 0 of same length of input

See: https://www.youtube.com/watch?v=Ks1pw1X22y4&t=233s
'''

start = '1010'

a = start
b = None

i=0

while b != start and i<20:
	i+=1
	head = str(int(a[-1]) ^ int(a[-2]))
	b = head + a[0:3]
	
	print(f'a: {a}')
	print(f'b: {b}')
	print()
		
	a = b

print(f'num iterations: {i}')

