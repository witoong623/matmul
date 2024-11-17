import struct
import time

import numpy as np


# load data from .mat
def load_float32_array(filepath):
    ''' Load array data from binary file in Python list.\n
        Caller must interpret the data as intended by caller
    '''
    arr = []
    with open(filepath, 'rb') as f:
        A_data = f.read()
        for i in range(0, len(A_data), 4):
            element_data = A_data[i:i+4]
            assert len(element_data) == 4
            arr.append(struct.unpack('f', element_data)[0])
    return arr

# square matrix size
N = 128

A = load_float32_array('A_128.mat')
B = load_float32_array('B_128.mat')
target_C = load_float32_array('C_128.mat')

assert len(A) == N * N
assert len(B) == N * N
assert len(target_C) == N * N

def matmul(A, B, M, K, N) -> list[float]:
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
    for row in range(N):
        for col in range(N):
            # first 2 loops are for each element of output matrix
            for i in range(N):
                # if matrix A is MxK, B is KxN, then third loop is for K times
                # to loop over all elements to do K multiplications and K-1 additions
                C[row * N + col] += A[row * N + i] * B[i * N + col]

    return C

C = matmul(A, B, N, N, N)
C = np.array(C, dtype=np.float32)
target_C = np.array(target_C, dtype=np.float32)
np.testing.assert_allclose(C, target_C, rtol=1e-5, atol=1e-5)
