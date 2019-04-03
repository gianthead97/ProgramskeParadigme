import constraint


problem = constraint.Problem()

def ogranicenje(jedinice, dvojke, petice, desetice, dvadesetice):
    return 50 == jedinice + 2*dvojke + 5*petice + 10*desetice + 20*dvadesetice


problem.addVariable("1", range(0, 51))
problem.addVariable("2", range(0, 26))
problem.addVariable("5", range(0, 11))
problem.addVariable("10", range(0, 6))
problem.addVariable("20", range(0, 3))

problem.addConstraint(ogranicenje, ["1", "2", "5", "10", "20"])

for resenje in problem.getSolutions():
    print (resenje)