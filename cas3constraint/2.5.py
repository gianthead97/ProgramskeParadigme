import constraint

def ogranicenje1(x, z):
    return x >= z

def ogranicenje2(x, y, z):
    return 2*x + y*x + z <= 34

problem = constraint.Problem()

problem.addVariable("x", range(1, 91))
problem.addVariable("y", range(2, 60, 2))
problem.addVariable("z", [x*x for x in range(1, 11)])

problem.addConstraint(ogranicenje1, "xz")
problem.addConstraint(ogranicenje2, "xyz")

for r in problem.getSolutions():
    print (f'x = {r["x"]} y = {r["y"]} z = {r["z"]}')