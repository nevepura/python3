# import argv to read argument variables
from sys import argv

# reads 2 argvs
script, filename = argv

# open yo file
txt = open(filename)

print(f"Look at the contents of the {filename} file:")
# i'm gonna see it!
print(txt.read())
txt.close()

file_again = input("tell me another file name:\n> ")
txt_again = open(file_again)


print(txt_again.read())
txt_again.close()