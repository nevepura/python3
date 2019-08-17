'''
kwargs: pass a dictionary as argument
pro: you don't need to know how many items are in the dictionary
'''

def print_kwargs(**kwargs):
    print(kwargs)

def print_values(**kwargs):
    # items() returns a list of couples (key, value) of the dictionary
    for key, value in kwargs.items():
        print("{0} -> {1}".format(key, value))

#print_kwargs(primo='pippo', secondo='pluto', terzo='paperino')
print_values(primo='pippo', secondo='pluto', terzo='paperino')