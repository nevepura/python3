'''
rimuove da un file i caratteri ch e copia il file snellito in ris.txt
'''

with open("devdeps.txt", "r") as f:
	with open ("ris.txt", "w") as out:
		for line in f:
			for ch in line:
				if ch != ":" and ch!= "\"" and ch!= ",":
					out.write(ch)

