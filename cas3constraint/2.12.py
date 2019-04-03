import constraint

def problem_to_row(x):
    row = ""
    x = x // 2
    for i in range(1, 9):
        if (x == 0):
            pass
        if x % 2 == 1:
            row += "T"
        else:
            row += "-"
        x = x // 2
    return row + "\n"

problem = constraint.Problem()

problem.addVariables("12345678", [2**x for x in range(1,9)])

problem.addConstraint(constraint.AllDifferentConstraint())

#print(problem.getSolution())

for resenje in problem.getSolutions():
    for i in range(1, 9):
        print(problem_to_row(resenje[str(i)]))
    print ('##############################################################')