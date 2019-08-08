# list comprehension
# print multiples of 4
mult4 = [i*4 for i in range(1,11)]
print ("multiples of 4: ", mult4)

# set comprehension
# print consonants
vowels = {'a','e','i','o','u'}
consonants = set()
{consonants.add(i) for i in "abcdefghilmnopqrstuvz" if i not in vowels}
print (consonants)

# dictionary comprehension
# lets make misters with id
names = ["Brown", "Pink", "Blue", "White", 'Orange', 'Purple', 'Black']
ids = [i for i in range (0, len(names))]
misters = {id: 'Mr. '+ names[id] for id in ids }
print(misters)

# the functions MAP and FILTER are some kind of comprehension

def isOdd(n):
	if 	n%2 == 1:
		return True
	else:
		return False

# MAP: map(function, sequence) calculates the function over all the elements of the sequence; returns an iterable

odds = map(isOdd, range(10))
#print(odds)
#print(list(odds))


oddset = map(isOdd, {1,3,5,7,8})
#print(oddset)
#print(set(oddset)) # funny set reduces elements to 2: True and False only (no repetitions)

# FILTER: filter(function, sequence) returns an iterable containing all the elements who pass through the filter. 
# the function here returns True or False

def isPrime(n):
	if n == 0 or n == 1:
		return False
	h = n//2
	for i in range (h,2,-1):
		#print (i)
		if n%i==0:
			#print('false, a divisor is: ',i)
			return False
	#print ('yeah, ',n,' is a prime!')
	return True


#isPrime(26)
#isPrime(29)

primes = filter(isPrime, range(30))
#print(list(primes))