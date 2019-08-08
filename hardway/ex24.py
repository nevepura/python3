print("Practice everything")
print('You\'d need 2 know \'bout escapezwith \\ that too:')
print('newlines \n and tabs \t.')

poem = """
    \tStupid fuckin\' poem
    with logic and stuff
    ok,, more lines
    \n\t tired, done.
"""

print('-----{}-----'.format(poem))

def secret_formula(started):
    a = started * 500
    b = a / 1000
    c = b / 100
    return a, b, c

start_point = 1000

beans, jars, crates = secret_formula(start_point)

print(f'with a starting point of {start_point} we\'d have {beans} beans, {jars} jars, {crates} crates')

# other way
start_point /= 10
formula = secret_formula(start_point)
print('with a starting point of {} we\'d have {} beans, {} jars, {} crates'.format(start_point, *formula))
