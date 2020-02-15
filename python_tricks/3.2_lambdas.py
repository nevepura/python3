# easy
add3 = lambda x, y, z : x + y + z
print(add3(4,3,3))

# inline
print(f"2 * 3 is: {(lambda x, y : x * y)(2, 3)}") 

# sorting tuples
tuples = [(1, 0.7), (2, 0.3), (3, 0.5)]
print(sorted(tuples, key = lambda x : x[1], reverse = False))
print(tuples) # no side effect on tuples by sorted()