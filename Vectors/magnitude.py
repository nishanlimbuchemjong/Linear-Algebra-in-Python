"""
Find the magnitude of the vector: v = [6, 8, -10]
"""
import math

v = [6, 8, -10]

magnitude = math.sqrt(sum((v[i]**2) for i in range(len(v))))

print(f"Magnitude of vector '{v}' is {magnitude:.4f}")
