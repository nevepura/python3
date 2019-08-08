# ex5.py
# printing with format string
name = 'Pippo'
age = 12
height = 170
height_inches = round(height / 2.54)
weight = 87
weight_pounds = round(weight * 2.20462, 2) # lbs = pounds
eyes = "brown"
teeth = "yellow"
hair = "brown"

print(f"Let's talk about {name}")
print(f'He is {height} cm tall')
print(f"He is {weight} kg heavy")
print(f"he's got {eyes} eyes and {hair} hair")
total = age + height + weight
print(f"lets sum age, height and weight!: {age} + {height} + {weight} = {total}. Happy now?")

print(f"height in inches: {height_inches}")
print(f"weight in lbs: {weight_pounds}")
