import mendeleev as md


'''
All the symbols of the periodic table
'''
elems = md.get_all_elements()
symbols = set(map(lambda el : el.symbol, elems))


'''
Given a name, transform it to a list of chemical symbols present in that name. 
'''
def symbolify(name : str):
	acc = []


	i = 0
	while i < len(name):
		step = 1
		
		if i +1 < len(name) and (name[i].upper() + name[i+1]) in symbols:
			#print(f'match two elements "{name[i:i+2]}"" at index {i}')
			acc.append((name[i].upper() + name[i+1]))
			step = 2

		elif name[i:i+1].upper() in symbols:
			#print(f'match one element "{name[i:i+1]}"" at index {i}')
			acc.append(name[i:i+1].upper())

		i += step

	return acc


def main():
	name = input("Give a name to inspect: ")

	#print(f'symbols: {symbols}')
	res = symbolify(name)
	print(res)


if __name__ == "__main__":
	main()
