
import numpy as np


def is_invertible(matrix):
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("The matrix must be square (nxn)")
    determinant = np.linalg.det(matrix)
    return determinant != 0


def invert_matrix(matrix):
    n = matrix.shape[0]
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("The matrix must be square (nxn)")
    identity_matrix = np.eye(n)
    augmented_matrix = np.hstack((matrix, identity_matrix))
    for i in range(n):
        if augmented_matrix[i, i] == 0:
            for j in range(i + 1, n):
                if augmented_matrix[j, i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    break
            else:
                raise ValueError("Matrix is singular and cannot be inverted.")
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        for j in range(n):
            if i != j:
                augmented_matrix[j] = augmented_matrix[j] - augmented_matrix[i] * augmented_matrix[j, i]
    inverse_matrix = augmented_matrix[:, n:]
    return inverse_matrix


def lu_decomposition(matrix):
    n = matrix.shape[0]
    L = np.zeros_like(matrix)
    U = np.zeros_like(matrix)
    for i in range(n):
        L[i, i] = 1
        for j in range(i, n):
            U[i, j] = matrix[i, j] - np.dot(L[i, :i], U[:i, j])
        for j in range(i + 1, n):
            L[j, i] = (matrix[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]
    return L, U


def forward_substitution(Lower, vector):
    n = Lower.shape[0]
    y = np.zeros_like(vector, dtype=np.float64)
    for i in range(n):
        y[i] = vector[i] - np.dot(Lower[i, :i], y[:i])
    return y


def backward_substitution(Upper, y):
    n = Upper.shape[0]
    x = np.zeros_like(y, dtype=np.float64)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(Upper[i, i + 1:], x[i + 1:])) / Upper[i, i]
    return x


def solve_linear_equations(A, b):
    L, U = lu_decomposition(A)
    print("L:\n", L)
    print("U:\n", U)
    y = forward_substitution(L, b)
    print("y:\n", y)
    x = backward_substitution(U, y)
    return x

def main(A=None,b=None):
    """A = np.array([[1, 4, -3],
            [-2, 1, 5],
            [3, 2, 1]])"""

    if not is_invertible(A):
        raise ValueError("Matrix isn't invertible")

    """b = np.array([1, 2, 3])"""
    x = solve_linear_equations(A, b)
    print(f"Solution of Ax = b: {x}")
    return x

if __name__ == '__main__':
    main()