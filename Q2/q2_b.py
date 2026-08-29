import numpy as np

from q2_a import gaussian_elimination_pivot




A = [
    [2, -6, -1],
    [-3, -1, 7],
    [-8, 1, -2]
]

b = [
    -38,
    -34,
    -20
]


# =====================================================
# Solve the system
# =====================================================

solution = gaussian_elimination_pivot(A, b)


# =====================================================
# Display the solution
# =====================================================

print("Solution of the given system:")

print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])