'''
Contents: 
format characters with backslash

'''

tabby = "\tI'm tabbed in."
persian = "I live in\nmultiple lines."
bach = "I have \\ backslash in me. \\See?"

fat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnop\n\t* Grass
"""

fat2 = '''
I'll do the same list:
\t* Cat food
\t* Fishies
\t* Catnop\n\t* Grass
'''

'''
print(tabby,'\n', persian, '\n', bach,'\n')
print(fat)
print(fat2)

'''

carriage_return = '\r'
tab = '\t'
vertical_tab = '\v'

stu = "this is a stupid {} string"
print(stu.format(carriage_return))