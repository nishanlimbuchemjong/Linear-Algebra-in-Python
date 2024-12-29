import sympy as sp

def solve_trigonometric_equation(user_equn):
    # defining the variables:
    x = sp.symbols('x')

    left, right = user_equn.split('=')
    eqn = sp.Eq(sp.sympify(left), sp.sympify(right))
    
    # solving the equation for x
    solution = sp.solveset(eqn, x, domain=sp.Interval(0, 2*sp.pi))

    # converting set into list
    solution_list = list(solution)
    
    return solution_list

user_equn = input("Enter a trigonometric equation: ")

solution = solve_trigonometric_equation(user_equn)

print(f"Solutions is given to you: {solution}")
