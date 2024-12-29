"""
    solve the equation: 
        2cos^2(x) - 1 = 0
    
    solution,
        cos(x) = (1/2)^2
"""
import math

def solve_cosine_equation():
    # calculating the possible value of cos(x)
    cos_x = math.sqrt(1/2)

    solution = []

    angle_in_radians = [
        math.acos(cos_x),
        math.acos(-cos_x)
    ]

    # converting angle in radians to angle in degrees
    solution = [math.degrees(angle) for angle in angle_in_radians]

    # since cosine is periodic, gives the solution within the range [0, 360]
    solution += [360 - angle for angle in solution]

    return solution

result = solve_cosine_equation()
print("The required solutions are: ")
for i in result:
    print(f"{i} degree")