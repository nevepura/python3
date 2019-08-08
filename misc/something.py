
def rewind(f):
	print('rewinding...')
	f.seek(0)

def printer(f):
	s = f.readline()
	print(s, end='')


my_file = open("input.txt",'r')
mf = my_file

s1 = mf.readline()
d = len(s1)

print(s1)
print(mf.readline(), end='')

mf.seek(d)
print(mf.readline(), end='')