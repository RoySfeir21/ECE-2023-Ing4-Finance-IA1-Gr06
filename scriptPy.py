
from constraint import Problem
from constraint import AllDifferentConstraint
from constraint import InSetConstraint

def solve_sudoku(grid):
    # Cr�ation du probl�me CSP
    problem = Problem()

    # Ajout des variables
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                # Les cases vides sont repr�sent�es par des variables
                problem.addVariable((i, j), range(1, 10))
            else:
                # Les cases initialement remplies sont repr�sent�es par des contraintes
                problem.addConstraint(InSetConstraint([grid[i][j]]), [(i, j)])

    # Ajout des contraintes
    # Contraintes de lignes
    for i in range(9):
        problem.addConstraint(AllDifferentConstraint(), [(i, j) for j in range(9) if grid[i][j] == 0])

    # Contraintes de colonnes
    for j in range(9):
        problem.addConstraint(AllDifferentConstraint(), [(i, j) for i in range(9) if grid[i][j] == 0])

    # Contraintes de r�gions
    for x in range(3):
        for y in range(3):
            problem.addConstraint(AllDifferentConstraint(), [(i, j) for i in range(x*3, (x+1)*3) for j in range(y*3, (y+1)*3) if grid[i][j] == 0])

    # R�solution du probl�me CSP avec la propagation de contraintes
    solution = problem.getSolution()

    # Cr�ation de la matrice solution
    solution_grid = [[0] * 9 for _ in range(9)]
    for (i, j), value in solution.items():
        solution_grid[i][j] = value

    return solution_grid


    r=solution_grid