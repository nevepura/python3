with open("aziende-new.pdf", "rb") as f:
	pdf = pdftotext.PDF(f)
	with open("out.txt",w) as o:
		for page in pdf:
			o.write(page)
