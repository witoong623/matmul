#ifndef UTILS_H
#define UTILS_H

#include <iostream>
#include <chrono>

class MatmalSpeedInfo {
public:
  // number of floating point operations for matmul in GFLOPs
  double FLOPs;
  // number of floating point operations per second in GFLOPS
  double FLOPS;
  // elapsed time in seconds
  double elapsed;
  // row of first matrix
  int M;
  // column of the second matrix
  int N;
  // column of the first matrix and row of the second matrix
  int K;

  MatmalSpeedInfo(double flops, double flops_per_sec, double elapsed_time, int m, int n, int k)
      : FLOPs(flops), FLOPS(flops_per_sec), elapsed(elapsed_time), M(m), N(n), K(k) {}
};

inline MatmalSpeedInfo get_speed_information(int M, int N, int K,
    std::chrono::high_resolution_clock::time_point start, std::chrono::high_resolution_clock::time_point end) {
  double elapsed_nano = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
  double elapsed_sec = elapsed_nano / 1e9;
  double GFLOPs = (2 * K - 1) * M * N / 1e9;
  double GFLOPS =  GFLOPs / (elapsed_nano / 1e9);

  return MatmalSpeedInfo(GFLOPs, GFLOPS, elapsed_sec, M, N, K);
}

#endif
