#!/usr/bin/env python 

import random

x = random.randint(1, 100)

ime = raw_input("Unesite Vase ime: ")

print "Zdravo {0:s}. :)\n".format(ime)
print "Zamislio sam neki broj od 1 do 100 da li mozes da pogodis koji je to broj?\n"

while True:
    tmp = int(raw_input("Unesi broj: "))
    if tmp == x:
        print "BRAVO!!! Pogodio si! Zamislio sam {0:d}. Bilo je lepo igrati se sa tobom!...\n".format(x)
        break
    elif tmp < x:
        print "Broj koji sam zamislio je VECI od {0:d}".format(tmp)
    else:
        print "Broj koji sam zamislio je MANJI od {0:d}".format(tmp)