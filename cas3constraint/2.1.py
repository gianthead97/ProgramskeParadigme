import constraint

problem = constraint.Problem()

problem.addVariable('x', 'abc')
problem.addVariable('y', [1, 2, 3])
problem.addVariable('z', [0.1, 0.2, 0.3])



def ogranicenje(y, z):
    return y / 10.0 == z

problem.addConstraint(ogranicenje, ['y', 'z'])
resenja = problem.getSolutions()

print (resenja)