import constraint
import math




def tabla_resenja(r):
    tabla = ""
    for i in range(1, 9):
        tmp = 2 ** r[str(i)]
        m = 2**7
        while m > 0:
            if tmp % 2 == 1:
                tabla += "D"
            else:
                tabla += "-"
            tmp = tmp // 2
            m = m // 2
        tabla += "\n"
    return tabla

problem = constraint.Problem()


problem.addVariables("12345678", range(0, 8))

problem.addConstraint(constraint.AllDifferentConstraint())


for k1 in range(1, 9):
    for k2 in range(1, 9):
        if k1 < k2:
            def ogranicenje(vrsta1, vrsta2, kolona1 = k1, kolona2 = k2):
                if math.fabs(vrsta1 - vrsta2) != math.fabs(kolona1 - kolona2):
                    return True
            problem.addConstraint(ogranicenje, [str(k1), str(k2)])


t = 0
for resenje in problem.getSolutions():
    t += 1
    print (tabla_resenja(resenje))
    print ("--------------------")

print (t)
