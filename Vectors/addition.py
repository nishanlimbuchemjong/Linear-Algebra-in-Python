"""
Given:
    a = [1, 2, 3]
    b = [4, 5, 6]
Vector addition of 2a + 3b = ?

"""
a = [1, 2, 3]
b = [4, 5, 6]
sum = []

for i in range(len(a)):
    sum.append(2*a[i] + 3*b[i])

print(f"Sum = {sum}")
