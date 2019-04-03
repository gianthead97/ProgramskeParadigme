#!/usr/bin/env python

import random

def ispisi_tablu(tabla):
    print "\n   TABLA   \n"
    print " 1   2   3"
    print "  --- --- ---"
    indeks = 1
    for i in tabla:
        print indeks , "|", i[0], "|", i[1], "|", i[2], "|"
        print "  --- --- ---"
        indeks += 1
    print "\n"

def pobedio(tabla):
    if (tabla[0][0] != "-" and tabla[0][2] != "-") and ((tabla[0][0] == tabla[1][1] == tabla[2][2]) or (tabla[0][2] == tabla[1][1] == tabla[2][0])):
        return True
    for i in range(1, 3):
        if (tabla[0][i] != "-" and tabla[i][0] != "-") and ((tabla[0][i] == tabla[1][i] == tabla[2][i]) or (tabla[i][0] == tabla[i][1] == tabla[i][2])):
            return True
    return False


def ucitaj_koordinate(ime):
    while True:
        print "{0:s} unesite koordinate polja koje zelite da popunite u posebnim linijama:\n".format(ime)
        x = int(raw_input("Unesite vrstu: "))
        y = int(raw_input("Unesite koordinatu: "))
        if 1 <= x <= 3 and 1 <= x <= 3:
            return x-1, y-1
        else:
            print "Morate uneti brojeve 1, 2 ili 3\n"


def korak(igrac):
    while True:
        x, y = ucitaj_koordinate(igrac[0])
        if tabla[x][y] == "-":
            tabla[x][y] = igrac[1]
            ispisi_tablu(tabla)
            break
        else:
            print tabla[x][y]
            print "Uneto je popunjeno polje.\n"


ime1 = raw_input("Unesite ime prvog igraca: ")
print "Zdravo {0:s}\n".format(ime1)
ime2 = raw_input("Unesite ime drugog igraca: ")
print "Zdravo {0:s}\n".format(ime2)

indikator = random.randint(1, 2)
if 1 == indikator:
    prvi_igrac = (ime1, "X")
    drugi_igrac = (ime2, "O")
else:
    prvi_igrac = (ime2, "X")
    drugi_igrac = (ime1, "O")


print "Igrac {0:s} igra prvi. \n".format(prvi_igrac)
print "X : {0:s}\n".format(prvi_igrac[0])
print "O : {0:s}\n".format(drugi_igrac[0])

tabla = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


print "Zapocnimo igru\n"

ispisi_tablu(tabla)



na_redu = 0
iteracija = 0
igraci = [prvi_igrac, drugi_igrac]
while iteracija < 9:
    korak(igraci[na_redu])
    if pobedio(tabla) == True:
        print "Bravo!!! Igrac {0:s} je pobedio!\n".format(igraci[na_redu][0])
        break
    na_redu = (na_redu + 1) % 2
    iteracija = iteracija + 1


if iteracija == 9:
    print "NERESENO! Pokusajte ponovo.\n"