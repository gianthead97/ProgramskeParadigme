import constraint   
import os


n = int(input("Unesite duzinu magicne sekvence: "))


problem = constraint.Problem()


def ispisi(resenje, n):
    print ('(', end = '')
    i = 0
    for v in resenje.values():
        i += 1
        if i == n:
            print (v, end = '')
        else:
            print (v, end = ',')
    print (')')
        


def dodatni_test(resenje):
    for i in range(n):
        if resenje[i] != list(resenje.values()).count(i):
            return False
    return True

problem.addVariables(range(n), range(n))

problem.addConstraint(constraint.ExactSumConstraint(n))


for r in problem.getSolutions():
    if dodatni_test(r):
        ispisi(r, n)


