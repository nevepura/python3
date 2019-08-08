# this lesson is about:
# f-strings and nesting;
# format()

# boolean variable 'hilarious' used to format a string in latter steps.
# first you declare a variable
hilarious = False
# then you prepare a string with brackets"
evaluation = "Isn't that joke funny?! {}"
# then you use format() to put that var into brackets. Noice"
print(evaluation.format(hilarious))

a = "left"
b = 'right'
ab = a + b
print(f'ab equals: {ab}')

n = 10 
o1 = f"I have {n} rabbits" # first f-string
print(o1)
o2 = f"Maybe you don't know that {o1}" # nesting first f-string into this one
print(o2)
print(f"Ashley said that {o2} and {a}") # nesting again

# breaking the code

print( "pipuz {}")
print( "pipuz {a}")
#print(f"pipuz {}") # broken: f-string, empty espression is not allowed. This is why you wanna use format() with emtpy brackets.

k = "pipuz {}"
print(k.format(a))

# print(f"pom{k}}") # BROKEN: can't put random single brackets in f-string.
print(f'ciao {a}' + f" di nuovo ciao {b}") # two f-strings chained

x = 3
y = 4
print(f"{x*y*10}") # you don't need to put variables, you can also make calculations