import constraint

def ogranicenje1(h, k):
    return 300*h + 120*k <= 20000

def ogranicenje2(h, k):
    return 10*h + 12*k <= 20 * 60


problem = constraint.Problem()

problem.addVariables("hk", range(1, 101))
problem.addConstraint(ogranicenje1, "hk")
problem.addConstraint(ogranicenje2, "hk")

max_k = 0
max_h = 0
max_zarada = float('-inf')

for resenje in problem.getSolutions():
    zarada = (7*resenje["h"] + 9*resenje["k"])
    if zarada > max_zarada:
        max_zarada = zarada
        max_k = resenje["k"]
        max_h = resenje["h"]


#print (problem.getSolutions())
print (f'Max zarada je {max_zarada}, od {max_k} kifli i {max_h} hlebova')
