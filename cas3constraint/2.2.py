import constraint


def ogranicenje(a, b, c):
    return (a*100 + b*10 +c) % (a + b + c) == 0

problem = constraint.Problem()


problem.addVariables("BC", range(0,10))
problem.addVariable("A", range(1, 10))



problem.addConstraint(ogranicenje, ["A", "B", "C"])

min_vrednost = float('inf')
min_resenje = 0
for resenje in problem.getSolutions():
    tmp_vrednost = (resenje["A"]*100 + resenje["B"]*10 + resenje["C"]) / (resenje["A"] + resenje["B"] + resenje["C"])
    if min_vrednost > tmp_vrednost:
        min_vrednost = tmp_vrednost
        min_resenje = resenje



print(min_resenje)  
