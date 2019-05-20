# gotta do side effects!

names = ['bob', 'sam', 'hateful', 'jane']

for name in names:
	name = 'kim'

# print (names)
# oops, no side effects here
# name is a local variable


for i in range(len(names)):
	names[i] = 'chuck'
# it works, but with effort. 
# 2 functions to use (len and range)
# plus less readability

# print (names)

for i, name in enumerate(names):
	if (i%2==1):
		names[i] = 'kim' + str(i)
# here you have both index and item in the same loop. Comfy.

# print(names)

print(list(enumerate(names))) 
# [(0, 'chuck'), (1, 'kim1'), (2, 'chuck'), (3, 'kim3')]

'''
The enumerate object is an array of couples.
Each couple is made of:
	index
	corresponding element in the enumerated array
'''

# very nice!