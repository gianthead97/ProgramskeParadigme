import constraint   
import os


n = int(input("Unesite duzinu magicne sekvence: "))


problem = constraint.Problem()


problem.addVariables(range(0, n), range(0, n))


def ogranicenje(i, lista):
    br_poj = 0
    for x in lista:
        if i == x:
            br_poj += 1
    return i == br_poj

for i in range(0, n):
    problem.addConstraint(ogranicenje, [i, [x for x in range(0, n)]])

print (problem.getSolution())
