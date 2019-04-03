#!/usr/bin/env python

import random
import numpy
n = int(raw_input("Unesite broj iteracija: "))

A = 0
B = 0
for i in range(n):
    print "Tacka:" 
    x = random.random()
    y = random.random()
    print "({0:f}, {1:f})\n".format(x, y)
    if (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.5 ** 2:
        A += 1

print "Broj PI aproksimiran MONTE CARLO metodom: {0:f}".format(4.0*A/n)


