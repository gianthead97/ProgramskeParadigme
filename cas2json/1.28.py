import json

komentari = {}
komentari['jednolinijski'] = []
komentari['viselinijski'] = []


with open("program.c", "r") as datoteka:
    sadrzaj_source = datoteka.read()
    

#print (sadrzaj_source)


kod_linija_po_linija = sadrzaj_source.split("\n")
#print(kod_linija_po_linija)

for linija in kod_linija_po_linija:
    if linija[:2] == "//":
        komentari['jednolinijski'].append(linija[2:])
i = 0
while i < len(kod_linija_po_linija):
    if kod_linija_po_linija[i][:2] == "/*":
        stringbuffer = ""
        i += 1
        while kod_linija_po_linija[i][:2] != "*/":
            stringbuffer += (kod_linija_po_linija[i] + "\n")
            i += 1
        i -= 1
        komentari['viselinijski'].append(stringbuffer)
    i += 1



komentari['jednolinijski'] = list(map(lambda x: x.strip(), komentari['jednolinijski']))
komentari['viselinijski'] = list(map(lambda x: x.strip(), komentari['viselinijski']))



f = open("komentari.json", "w")
json.dump(komentari, f)
f.close()

