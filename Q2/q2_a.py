import numpy as np


def gaussian_elimination_pivot(A, b):

    
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)


    for k in range(n - 1):

        pivot_row = k + np.argmax(np.abs(A[k:n, k]))

        if abs(A[pivot_row, k]) < 1e-12:
            raise ValueError("The system has no unique solution.")

       
        A[[k, pivot_row]] = A[[pivot_row, k]]
        b[[k, pivot_row]] = b[[pivot_row, k]]

       
        for i in range(k + 1, n):

            factor = A[i, k] / A[k, k]

            A[i, k:] = A[i, k:] - factor * A[k, k:]
            b[i] = b[i] - factor * b[k]


    x = np.zeros(n)

    for i in range(n - 1, -1, -1):

        x[i] = (
            b[i] - np.dot(A[i, i + 1:], x[i + 1:])
        ) / A[i, i]

    return x


A = [
    [2, 1],
    [4, 3]
]

b = [
    5,
    11
]

solution = gaussian_elimination_pivot(A, b)

print("Solution:")
print(solution)