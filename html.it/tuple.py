t1 = (1,2,3)
t2 = (1.1, 2, 4.5)
# tupla di un solo elemento
t3 = ("ciao",)
print ("type of t3 is: ",type(t3))

t4 = ()
print ("type of t4 is: ",type(t4))

# operazioni supportate:
# indexing, slicing, contenimento, concat, prodotto
t5 = ("oddish", "gloom", "vileplume", "bellossom")
print ("t5 is: ", t5)
#t5[1]
#t5[:2]

'''
'in' operator
returns true if the element is contained in the tuple
'''
print ('vileplume' in t5) #true
print('jolteon' in t5) #false
# only checks elements
t55 = ('abra', 'kadabra', ('drowzee', 'hypno'))
print('t55#1', ('drowzee', 'hypno') in t55) #true, because it's an element of the tuple
print('t55#2',('abra', 'kadabra') in t55) #false, it's a portion of the tuple


t6 = t5+ t1
print (t6)
t7 = (t5 * 2)
print(t7)

t8 = ('unknown', 'bulba', 'ivy', 'bulba','venu', 'ivy')
i1 = t8.index('bulba')
i2 = t8.count('bulba')
print (i1)
print(i2)