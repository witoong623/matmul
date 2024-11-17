import argparse

import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create data for training')
    parser.add_argument('--N', type=int, default=1024, help='matrix size')
    args = parser.parse_args()

    A = np.random.rand(args.N, args.N).astype(np.float32)
    B = np.random.rand(args.N, args.N).astype(np.float32)
    C = A.dot(B)

    print(f'Strides of array A is {A.strides}')
    print(f'Strides of array B is {B.strides}')
    print(f'Strides of array C is {C.strides}')
    # if matrix is 1024 * 1024, strides is (4096, 4)
    # if we want to access A[i, j], we need to calculate offset = i * 4096 + j * 4

    # write all matrix to file
    with open(f'A_{args.N}.mat', mode='wb') as f:
        f.write(A.data)

    # create .npy file for debugging purpose
    np.save(f'A_{args.N}.npy', A)

    with open(f'B_{args.N}.mat', mode='wb') as f:
        f.write(B.data)

    np.save(f'B_{args.N}.npy', B)

    with open(f'C_{args.N}.mat', mode='wb') as f:
        f.write(C.data)

    np.save(f'C_{args.N}.npy', C)
