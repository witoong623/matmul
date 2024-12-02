import struct
from dataclasses import dataclass


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


@dataclass
class MatmalSpeedInfo:
    '''
    Data class to hold matrix multiplication speed information
    '''
    # number of floating point operations for matmul in GFLOPs
    FLOPs: float
    # number of floating point operations per second in GFLOPS
    FLOPS: float
    # elapsed time in seconds
    elapsed: float
    # row of first matrix
    M: int
    # column of the second matrix
    N: int
    # column of the first matrix and row of the second matrix
    K: int


def get_speed_informaiton(M, N, K, start, end) -> MatmalSpeedInfo:
    ''' Get speed information for matrix multiplication
    '''
    elapsed = (end - start) / 1e9
    GFLOPs = (2 * K - 1) * M * N / 1e9

    return MatmalSpeedInfo(FLOPs=GFLOPs, FLOPS=GFLOPs / elapsed, elapsed=elapsed, M=M, N=N, K=K)
