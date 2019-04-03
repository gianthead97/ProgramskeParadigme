niska1 = input("Unesite nisku 1:")
niska2 = input("Unesite nisku 2:")


if len(niska1) >= len(niska2):
	n = niska1.count(niska2)

	if n > 0:
		i = niska1.find(niska2)
		niska1 = niska1[0:i] + '$' + niska1[i + len(niska2) : ]
		print(niska1)
	else:
		print('-'.join([niska1, niska2]))
else:
	print("Duzina niske {0:s} je {1:d}".format(niska2, len(niska2)))
