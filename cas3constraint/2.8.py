import constraint
def ogranicenje(a, b, c, d, e):
    uslov = (a < b < c < d < e)
    uslov = uslov and (a + b + c + d + e == 25)
    return uslov

problem = constraint.Problem()

problem.addVariables("abcdefghi", range(1, 10))

problem.addConstraint(ogranicenje, "abcde")
problem.addConstraint(ogranicenje, "fgchi")
problem.addConstraint(constraint.AllDifferentConstraint())

#a   f
# b g 
#  c
# h d
#i   e
for resenje in problem.getSolutions():
    print (f'{resenje["a"]}   {resenje["f"]}')
    print (f' {resenje["b"]} {resenje["g"]}')
    print (f'  {resenje["c"]}')
    print (f' {resenje["h"]} {resenje["d"]}')
    print (f'{resenje["i"]}   {resenje["e"]}')
    print ('----------------')
