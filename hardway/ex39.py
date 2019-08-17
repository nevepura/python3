'''
Dictionaries
Functions:
    items()
    get(): rispetto a [] permette di gestire il caso in cui manca la chiave
'''

states = {
    'Oregon' : 'OR',
    'California' : 'CA',
    'Florida' : 'FL',
}

cities = {
    'OR' : 'Portland',
    'CA' : 'San Francisco',
    'FL' : 'Jacksonville'
}

# print(states)
# print(states.items()) # dict items
# print(list(states.items())) # list of couples

for state, abbr in list(states.items()):
    print(f"{state} is abbreviated {abbr} and has city {cities[abbr]}")

print(states.get('Oregon'))
print(states.get('Maryland', 'Does not exist'))