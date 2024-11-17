import time

import numpy as np

from utils import load_float32_array, get_speed_informaiton


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

start = time.perf_counter_ns()
C = matmul(A, B, N, N, N)
end = time.perf_counter_ns()
speed_info = get_speed_informaiton(N, N, N, start, end)

print(f'GFLOPs for {N}x{N} matrix multiplication = {speed_info.FLOPs} GFLOPs')
print(f'Elapse {speed_info.elapsed} second, FLOPS = {speed_info.FLOPS:.5f} GFLOPS')

C = np.array(C, dtype=np.float32)
target_C = np.array(target_C, dtype=np.float32)
np.testing.assert_allclose(C, target_C, rtol=1e-5, atol=1e-5)
