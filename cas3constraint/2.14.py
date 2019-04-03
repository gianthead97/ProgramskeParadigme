import constraint, json
import sys
ime_datoteke = input("Unesite ime datoteke sa tabolom za sudoku: ")

try:
    with open(ime_datoteke, "r") as sudoku_datoteka:
        sudoku = json.load(sudoku_datoteka)
except IOError:
        print ("IOError ")
        exit()




problem = constraint.Problem()





for i in range(1, 10):
    problem.addVariables(range(i*10 + 1, i*10 + 10), range(1, 10))


i = 0




for red in sudoku:
    i += 1
    for j in range(1, 10):
        def ogranicenje(x, y = red[j-1]):
            return x == y
        if red[j-1] != 0:
            problem.addConstraint(ogranicenje, [i*10 + j])


for i in range(1, 10):
    problem.addConstraint(constraint.AllDifferentConstraint(), [i*10+j for j in range(1, 10)])

for i in range(1, 10):
    problem.addConstraint(constraint.AllDifferentConstraint(), [x*10+i for x in range(1, 10)])


problem.addConstraint(constraint.AllDifferentConstraint(), [11, 12, 13, 21, 22, 23, 31, 32, 33])
problem.addConstraint(constraint.AllDifferentConstraint(), [14, 15, 16, 24, 25, 26, 34, 35, 36])
problem.addConstraint(constraint.AllDifferentConstraint(), [17, 18, 19, 27, 28, 29, 37, 38, 39])

problem.addConstraint(constraint.AllDifferentConstraint(), [41, 42, 43, 51, 52, 53, 61, 62, 63])
problem.addConstraint(constraint.AllDifferentConstraint(), [44, 45, 46, 54, 55, 56, 64, 65, 66])
problem.addConstraint(constraint.AllDifferentConstraint(), [47, 48, 49, 57, 58, 59, 67, 68, 69])

problem.addConstraint(constraint.AllDifferentConstraint(), [71, 72, 73, 81, 82, 83, 91, 92, 93])
problem.addConstraint(constraint.AllDifferentConstraint(), [74, 75, 76, 84, 85, 86, 94, 95, 96])
problem.addConstraint(constraint.AllDifferentConstraint(), [77, 78, 79, 87, 88, 89, 97, 98, 99])

print("") 

resenje = problem.getSolution()
for i in range(1, 10):
    for j in range(1, 10):
        print(resenje[i*10+j], end='')
    print (" ")