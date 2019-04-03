import json

ime_datoteke = input("Unesite ime datoteke: ")

with open(ime_datoteke, "r") as datoteka:
    sadrzaj = datoteka.read()



n = int(input("Unesite n: "))

recnik = dict()
i = 0
while i < len(sadrzaj) - n:
    ngram = sadrzaj[i : i+n]

    if ngram in recnik:
        recnik[ngram] = recnik[ngram] + 1
    else: 
        recnik[ngram] = 1

    i = i + 1

f = open("rezultat.txt", "w")
json.dump(recnik, f)
f.close()

#print (sadrzaj)