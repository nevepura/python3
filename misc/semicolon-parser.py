'''
Lo script fa il parsing del fine in input, carattere per carattere (scorre prima le righe, poi i caratteri).
Copia il file in input in output, aggiungendo un carattere 'newline' dopo ogni ';' incontrato nel file in input.
'''

with open("input.txt", "r") as f1:
	with open("output.txt", "w") as f2:
	  for line in f1:
	    for ch in line:
	    	f2.write(ch)
	    	if ch == ';' :
	    		f2.write("\n")