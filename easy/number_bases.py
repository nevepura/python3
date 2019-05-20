bina = 0b1 # binary
octa = 0o12 #octal
esad = 0xFF
ob = octa + bina
bo = bina + octa
be = bina + esad
eb = esad + bina

print ('ob: ',ob,'bo: ',bo,'be: ', be, 'eb: ', eb) # prints all  in base 10

#shifting
x = 0b0100 #4
print ('x: ',x)
x = x<<1
print ('x: ',x)
x = x<<1
print ('x: ',x)
x = x<<1
print ('x: ',x)

y = 0b10 #2
print ('y: ',y)
y = y>>1 #1
print ('y: ',y)
y = y>>1 #0
print ('y: ',y)
y = y>>1 #0
print ('y: ',y)

f = 10 
print ('f: ',f)
f= f>>1 # shifting, int f becomes binary
print ('f: ',f)

f= f>>1
print ('f: ',f)
f= f>>1
print ('f: ',f)

'''
f = 10.0
print ('f: ',f)
f= f>>1 # shifting float f is unsupported
print ('f: ',f)

f= f>>1
print ('f: ',f)
f= f>>1
print ('f: ',f)
'''