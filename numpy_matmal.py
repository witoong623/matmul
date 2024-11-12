import os
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import time

import numpy as np

# square matrix size
N = 1024

# each element of row and column multiply N time, and then sum N-1 times
# we do this for all NxN elements of output matrix, so N * N times
FLOPs = (2 * N - 1) * N * N

A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)

start = time.perf_counter_ns()
C = A.dot(B)
end = time.perf_counter_ns()

elapsed_time = (end - start) / 1e9

print(f'GFLOPs for {N}x{N} matrix multiplication = {FLOPs / 1e9} GFLOPs')
print(f'Elapse {elapsed_time} second, FLOPS = {(FLOPs / 1e9) / elapsed_time:.2f} GFLOPS')

# max theoretical FLOPS for my CPU at 3.6 (turbo 4.9) GHz, 32 FP32 operations per cycle
MAX_FLOPS_NORMAL = 3.6 * 32
MAX_FLOPS_TURBO = 4.9 * 32
print(f'Max theoretical FLOPS = {MAX_FLOPS_NORMAL} GFLOPS')
print(f'Max turbo theoretical FLOPS = {MAX_FLOPS_TURBO} GFLOPS')
