import numpy as np
from numpy.linalg import norm

# Utility functions

def is_diagonally_dominant(A):
    D = np.diag(np.abs(A))  # Diagonal coefficients
    S = np.sum(np.abs(A), axis=1) - D  # Sum of non-diagonal coefficients
    return np.all(D > S)


def is_square_matrix(A):
    return A.shape[0] == A.shape[1]

def gauss_seidel(A, b, X0=None, TOL=1e-16, N=15):
    n = len(A)
    k = 1
    if X0 is None:
        X0 = np.zeros_like(b, dtype=np.double)

    if is_diagonally_dominant(A):
        print('Matrix is diagonally dominant - performing Gauss-Seidel algorithm\n')

    print("Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, n + 1)]]))
    print("-----------------------------------------------------------------------------------------------")
    x = np.zeros(n, dtype=np.double)
    while k <= N:
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if norm(x - X0, np.inf) < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return tuple(x)

def main(A=None,b=None):
    """A = np.array([[3, -1, 1], [0, 1, -1], [1, 1, -2]])
    b = np.array([4, -1, -3])"""
    X0 = np.zeros_like(b)

    print("\nGauss-Seidel Method:")
    gauss_seidel_solution = gauss_seidel(A, b, X0)
    print("\nApproximate solution using Gauss-Seidel:", gauss_seidel_solution)
    return gauss_seidel_solution

if __name__ == "__main__":
    main()