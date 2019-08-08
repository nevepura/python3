# study drill 2: can you assign an object to a list on an out-of-range index? No.
elements = []
# elements[1] = 1 # error, index out of range

'''
Operations with lists:
append
extend: you can extend a list with any iterable, like a set or a tuple
insert(index, object)
remove(object)
pop(index): returns the popped item
clear
index
count
sort
reverse
copy
'''

list1 = [1,2,3,4]


list1.extend(('pipo', 'pupo'))
list1.extend({'cip', 'ciop', 'margherita'})

list1.clear()
print (list1)

list2d = [[1,2,3], [4,5,6]]
print(f"list2d : {list2d}")