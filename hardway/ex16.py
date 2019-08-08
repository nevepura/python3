from sys import argv

script, filename = argv

print(f"we are going to erase {filename}.")
print("If you don't want it, press CTRL-C (^C)")
print("if you do, press RETURN")
input("?\n> ")

print("Opening")
target = open(filename, 'w')

print("Truncating the file. Farewell.")
target.truncate()

print("Now, let's fill the truncated file with 2 new lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

total = f"{line1}\n{line2}\n{line3}\n"
target.write(total)


print("file written. Its contents are:")
target.close()
target = open(filename)
print(target.read())
target.close()