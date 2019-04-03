import constraint

def ogranicenje(a, b, c, d = 0, e = 0):
    return a + b + c + d + e == 38

def globalnoOgranicenje(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s):
    return a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s == 5 * 38

problem = constraint.Problem()

problem.addVariables("abcdefghijklmnopqrs", range(1, 22))

problem.addConstraint(constraint.AllDifferentConstraint())


problem.addConstraint(globalnoOgranicenje, "abcdefghijklmnopqrs")

problem.addConstraint(ogranicenje, "abc")
problem.addConstraint(ogranicenje, "defg")
problem.addConstraint(ogranicenje, "hijkl")
problem.addConstraint(ogranicenje, "mnop")
problem.addConstraint(ogranicenje, "qrs")


problem.addConstraint(ogranicenje, "adh")
problem.addConstraint(ogranicenje, "beim")
problem.addConstraint(ogranicenje, "cfjnq")
problem.addConstraint(ogranicenje, "rok")
problem.addConstraint(ogranicenje, "spl")

problem.addConstraint(ogranicenje, "cgl")
problem.addConstraint(ogranicenje, "bfkp")
problem.addConstraint(ogranicenje, "aejos")
problem.addConstraint(ogranicenje, "dinr")
problem.addConstraint(ogranicenje, "hmq")
print (problem.getSolution())

#for rez in problem.getSolutions():
#    print (f'    {rez["a"]},{rez["b"]},{rez["c"]}    ')
#    print (f'  {rez["d"]},{rez["e"]},{rez["f"]},{rez["g"]}  ')
#    print (f'{rez["h"]},{rez["i"]},{rez["j"]},{rez["k"]},{rez["l"]}')
#    print (f'  {rez["m"]},{rez["n"]},{rez["o"]},{rez["p"]}  ')
#    print (f'    {rez["q"]},{rez["r"]},{rez["s"]}    ')
#    print('---------------------------')