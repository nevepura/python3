import re

# compile(): compila un pattern in un 'regular expression object', che puo` essere usato da altri metodi come match() e search()
def search_pattern_in_string(pattern, string): 
	search = re.compile(pattern).search(string)
	if not search:
		return "Nay, no match"
	else:
		return "Aye, Found pattern: " + search.group()


'''
print(search_pattern_in_string('\D+\s\D+', 'my 1 name1 is1 jason1 bourne again'))


#sub()
str = 'Hi, write your name here: [HERE]'
str = re.sub('\[HERE\]', 'Pluto Paperino', str)
print(str)


#findall()
s = 'Ciao, iato, penare, ahia'
founds = re.findall('ia',s)
print (founds)
'''

'''
#match: cerca il match del pattern nella stringa, solo a partire dall'inizio della stringa
string = 'abcdef ghi'
pattern1 = 'abcdef g'
pattern2 = 'bcdef g'
ma = re.match (pattern1, string)
print(ma) # Match object
ma = re.match (pattern2, string)
print(ma) # None
'''

'''
#search(): cerca il pattern dentro la stringa, anche in posizioni intermedie
string = 'abcdef'
pat1 = 'bcd'
pat2 = 'def'
pat3 = 'df' # la ricerca fallisce per pattern non contigui
se1 = re.search(pat1,string) # Match object
se2 = re.search(pat2,string) # Match object
se3 = re.search(pat3,string) # None
print(se1)
print(se2)
print(se3)
'''

'''
#group
str = 'i am bob i am 35 and i have 2 cats. So lonely...'
pat = '(\w+)\s(\d\d)'
p = re.compile(pat)
found = p.search(str)
print (found)
print(found.group(0)) # all
print(found.group(1)) # first couple of parenthesis
print(found.group(2)) # second parenthesis
'''
'''
#split()
addresses = '127.0.0.1;192.168.0.1;92.56.7.8'
delimiter = ';'
splitted = re.split(delimiter, addresses)
print(splitted)
'''