from sys import argv

'''
script, first, second = argv
print("the script is called:", script)
print("first var is called:", first)
print("second var is called:", second)
#print("third var is called: ", third)
'''

name = input("What is your name? ")
script, surname = argv
print(f"I assume you are {name} {surname}")