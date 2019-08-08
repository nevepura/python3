
# Copies a file into another. Can you shorten it?

from sys import argv
from os.path import exists

script, inp, out = argv

myinput = open(inp)
indata = myinput.read()
myinput.close()

# funny, tells you the dimension of a text file in bytes
# print (f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(out)}")

print("Ready? Hit RETURN to continue, CTRL-C to abort")
input()

myoutput = open(out, 'a+')
myoutput.write(indata)

# NOTICE: if you wanna read from this file, you have to reset the pointer to the beginning
myoutput.seek(0)
testo = myoutput.read()
myoutput.close()

'''
# this works, but makes one more I/O operation
myoutput = open(out,'r')
testo = myoutput.read()
'''

print(f"now the {out} contains:\n{testo}")

myoutput.close()
