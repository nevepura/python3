s = 'are you still there'
print (s[0:2])
print (s[:3])
print (s[-3:-1])
print (s[5:])
print (s[-5:])

# containment operators: in, not in
print ('you' in s)
print (' you ' in s)
print ('yours' in s)
print ('yours' not in s)

#length
l = len(s)

#array length
arr = [1,2,3]
print (len(arr))

#dictionary length
dic = {1:25, 2:3, 3:44, 4:32}
print (len(dic))

#mixed
mixdic = {1:25, 2:3, 3:44, 4:32, 5:[3,4,5]}
print (len(mixdic))

#uppercase, lowercase
st = 'Ghana'
stu = st.upper()
stl = st.lower()

print(st, stu, stl)

#format # DOESN'T WORK! Maybe the guide is not updated
#stringa con placeholder
raggio = 8.4
area = 3.14 * raggio**2
circ = 2 * 3.14 * raggio
s = "L'area è {}, la circonferenza è {}."
s.format(area, circ)
print (s)