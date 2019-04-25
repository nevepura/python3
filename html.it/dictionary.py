# define couples
print('begin')

couples = {
    1: ['john', 'mary'],
    2: ['bob', 'sally'],
    3: ['craig',]
}

couples[4] = ['Pipps', 'Shirley']
del couples[2]
for i in couples:
    print (couples[i])

# 'in' operator checks if key is present in dict
'''
if 1 in couples:
  print('couples[1] esiste')
else:
  print('couples[1] non esiste')
if 5 in couples:
  print('couples[5] esiste')
else:
  print('couples[5] non esiste')
'''

# print
'''
for i in couples:
    a = couples[i]
    if len(a)==  2:
        print (str(a)+' is a couple')
    else:
        print (str(a)+' is not a couple')
    d.sort()
'''
#functions
'''
d = couples.copy()
print (d.keys())
print(d.values())
d.get(1,0) # get(key, default), returns key if present, default if not present
d.get(24,0) 
d.pop(3,0) #removes and return key if present, else returns default
d.popitem() #pops last item
d.update({6:66,7:78,8:83})}) # merge dictionary given as attribute with the invocation obj
d.clear() #empties dictionary
'''

