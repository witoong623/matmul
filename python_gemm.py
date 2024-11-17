import numpy as np
from numba import jit, float32
from numba.typed import List


def pure_python_matmul(A, B, M, K, N) -> list[float]:
    '''
    Perform matrix multiplication of two matrices A and B.
    Parameters:
    A (list of list of floats): The first matrix with dimensions M x K.
    B (list of list of floats): The second matrix with dimensions K x N.
    M (int): The number of rows in matrix A.
    K (int): The number of columns in matrix A and the number of rows in matrix B.
    N (int): The number of columns in matrix B.
    Returns:
    list of list of floats: The resulting matrix with dimensions M x N after multiplying A and B.
    '''
    C = [0] * (M * N)
    for row in range(M):
        for col in range(N):
            # first 2 loops are for each element of output matrix
            c = 0.0
            for i in range(K):
                # if matrix A is MxK, B is KxN, then third loop is for K times
                # to loop over all elements to do K multiplications and K-1 additions
                c += A[row * K + i] * B[i * K + col]
            # store result in temp variable (in registry?) to avoid accessing array memory 2K - 1 times
            C[row * N + col] = c

    return C


@jit()
def numba_matmul(A: list[float], B: list[float], M, K, N) -> list[float]:
    '''
    Perform matrix multiplication of two matrices A and B.
    Parameters:
    A (list of list of floats): The first matrix with dimensions M x K.
    B (list of list of floats): The second matrix with dimensions K x N.
    M (int): The number of rows in matrix A.
    K (int): The number of columns in matrix A and the number of rows in matrix B.
    N (int): The number of columns in matrix B.
    Returns:
    list of list of floats: The resulting matrix with dimensions M x N after multiplying A and B.
    '''
    C = np.zeros(M * N, dtype=np.float32)
    C = List(C)
    for row in range(M):
        for col in range(N):
            # first 2 loops are for each element of output matrix
            c = 0.0
            for i in range(K):
                # if matrix A is MxK, B is KxN, then third loop is for K times
                # to loop over all elements to do K multiplications and K-1 additions
                # this is float64 multiplication and addition, can't force it to float32
                c += A[row * K + i] * B[i * K + col]
            # store result in temp variable (in registry?) to avoid accessing array memory 2K - 1 times
            C[row * N + col] = c

    return C

matmul = numba_matmul

__all__ = ['matmul']
