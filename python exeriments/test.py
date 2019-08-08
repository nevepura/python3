from sys import argv

script, file = argv

target = open(file, 'w')
print('writing on file')
target.write("a new line\n")
target.write("second new line\n")
target.close()

target = open(file, 'r')
print('reading: \n' + target.read())
target.close()

target = open(file, 'w')
print('truncating file')



target = open(file, 'r')
print('after trunc file contains: \n' + target.read())
target.close()

target.close()