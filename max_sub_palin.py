
def sanitize(string):
	return string.replace(' ','')
	# qua puoi aggiungere altri tipi di sanificazione, ad es rimuovere punteggiatura.


def is_palin(string):
	if len(string) == 1 or len(string) == 0:
		return True

	elif len(string) == 2:
		return string[0] == string[1]

	# len>2
	else: 
		return string[0] == string[-1] and is_palin(string[1:-1])


def max_sub_palin(string):
	# remove blanks
	
	if is_palin(string):
		return len(string)

	else:
		return max(max_sub_palin(string[:-1]), max_sub_palin(string[1:]))





#max_sub_palin("abbecedario")
"""
print(is_palin("aeiou"))
print(is_palin("aeiiea"))
print(is_palin("ae"))
print(is_palin("''"))
print(is_palin("ae"))
print(is_palin("d"))
print(is_palin(""))
"""
string = "2a m babma03 2"
string = sanitize(string)
print(max_sub_palin(string))

