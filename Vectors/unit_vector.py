"""
Given:
    v = [4, -2, 1]
    find the unit vector of v

    [hint:
            u = v/|v|
    ]
"""
import math

v = [4, -2, 1]
sum = 0
unit_vector = []

# calculating the magnitude:
for i in range(len(v)):
    sum += (v[i])**2 

magnitude_v = math.sqrt(sum)

# calculating the unit vector of v:
for i in range(len(v)):
    unit_vector.append((v[i]/magnitude_v))

# printing the unit vector:
print(f"sum: {unit_vector}")