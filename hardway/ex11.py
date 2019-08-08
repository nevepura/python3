# Notice about END
# default end is '\n', so you go to a new line after print.
# you wanna change that, you change end
'''
print("tell me your age", end = ' ')
age = input()
print("how tall are you?", end = ' ')
height = input()
print(f"So, you are {age} years old, you are {height} cm tall.")
'''
# Any better way to do input? yeah!

secret = input("What is your secret? ")
print(f"Your secret is: {secret}")