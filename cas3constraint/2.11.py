import constraint

def ogranicenje1(d, e):
    return 100*e + 105*d <= 26000
def ogranicenje2(d, e):
    return 150*e + 170*d <= 51200
def ogranicenje3(d, e):
    return d + e <= 250

problem = constraint.Problem()

problem.addVariables("DE", range(1, 251))
problem.addConstraint(ogranicenje1, "DE")
problem.addConstraint(ogranicenje2, "DE")
problem.addConstraint(ogranicenje3, "DE")

max_d = 0
max_e = 0
max_zarada = float('-inf')
zarada = 0

for rez in problem.getSolutions():
    zarada = (150*5*rez['E'] + 170*6*rez['D']) - 100*rez['E'] - 105*rez['D']
    if zarada > max_zarada:
        max_zarada = zarada
        max_d = rez["D"]
        max_e = rez["E"]

print (f"Najbolja zarada je {max_zarada}, sa {max_e} Elixir programera i {max_d} Dart programera")