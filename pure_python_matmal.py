import time

import numpy as np

from utils import load_float32_array, get_speed_informaiton
from python_gemm import matmul


# square matrix size
N = 128

A = load_float32_array(f'A_{N}.mat')
B = load_float32_array(f'B_{N}.mat')
target_C = load_float32_array(f'C_{N}.mat')

assert len(A) == N * N
assert len(B) == N * N
assert len(target_C) == N * N

# converting list of floats to float32 numpy array will be faster
A = np.array(A, dtype=np.float32)
B = np.array(B, dtype=np.float32)

warnup = matmul(A, B, N, N, N)
start = time.perf_counter_ns()
C = matmul(A, B, N, N, N)
end = time.perf_counter_ns()
speed_info = get_speed_informaiton(N, N, N, start, end)

print(f'GFLOPs for {N}x{N} matrix multiplication = {speed_info.FLOPs} GFLOPs')
print(f'Elapse {speed_info.elapsed} second, FLOPS = {speed_info.FLOPS:.5f} GFLOPS')

C = np.array(C, dtype=np.float32)
target_C = np.array(target_C, dtype=np.float32)
np.testing.assert_allclose(C, target_C, rtol=1e-5, atol=1e-5)
