import constraint

def ogranicenje(t, w, o, f, u, r):
    return 2 * (t*100 + w*10 + o) == f*1000 + o*100 + u*10 + r


problem = constraint.Problem()

problem.addVariables("tf", range(1, 10))
problem.addVariables("wour", range(0,10))
problem.addConstraint(constraint.AllDifferentConstraint())
problem.addConstraint(ogranicenje, "twofur")


for r in problem.getSolutions():
    print (f' {r["t"]}{r["w"]}{r["o"]}')
    print (f' {r["t"]}{r["w"]}{r["o"]}')
    print (f'{r["f"]}{r["o"]}{r["u"]}{r["r"]}')
    print ('---------------')