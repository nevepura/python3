# Copies a file into another. Can you shorten it?

from sys import argv
from os.path import exists

script, inp, out = argv

# reading
indata = open(inp).read()
# writing
open(out, 'w+').write(indata)
# write returns the number of characters written. 
# can't chain read() after that.

