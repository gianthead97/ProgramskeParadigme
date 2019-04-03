import constraint

problem = constraint.Problem()

problem.addVariables("abcdefghi", range(1, 10))


# a  b  c
# d  e  f
# g  h  i

def ogranicenje(a, b, c, d, e, f, g, h, i):
    uslov = (a + b + c == 15)
    uslov = uslov and (d + e + f == 15)
    uslov = uslov and (g + h + i == 15)
    uslov = uslov and (a + d + g == 15)
    uslov = uslov and (b + e + h == 15)
    uslov = uslov and (c + f + i == 15)
    uslov = uslov and (a + e + i == 15)
    uslov = uslov and (c + e + g == 15)
    return uslov


problem.addConstraint(constraint.AllDifferentConstraint())
problem.addConstraint(ogranicenje, "abcdefghi")
for resenje in problem.getSolutions():
    print("{}  {}  {}".format(resenje["a"], resenje["b"], resenje["c"]))
    print("{}  {}  {}".format(resenje["d"], resenje["e"], resenje["f"]))
    print("{}  {}  {}".format(resenje["g"], resenje["h"], resenje["i"]))
    print("---------------------------")