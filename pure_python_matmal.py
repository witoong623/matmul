import time

import numpy as np

from utils import load_float32_array, get_speed_informaiton
from python_gemm import matmul


# square matrix size
N = 128

A = load_float32_array('A_128.mat')
B = load_float32_array('B_128.mat')
target_C = load_float32_array('C_128.mat')

assert len(A) == N * N
assert len(B) == N * N
assert len(target_C) == N * N

start = time.perf_counter_ns()
C = matmul(A, B, N, N, N)
end = time.perf_counter_ns()
speed_info = get_speed_informaiton(N, N, N, start, end)

print(f'GFLOPs for {N}x{N} matrix multiplication = {speed_info.FLOPs} GFLOPs')
print(f'Elapse {speed_info.elapsed} second, FLOPS = {speed_info.FLOPS:.5f} GFLOPS')

C = np.array(C, dtype=np.float32)
target_C = np.array(target_C, dtype=np.float32)
np.testing.assert_allclose(C, target_C, rtol=1e-5, atol=1e-5)
