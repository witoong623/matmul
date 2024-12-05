#include <cmath>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <string>

#include "utils.h"


constexpr int N = 1024;

void load_float32_array(std::string filepath, float* array, int size) {
  FILE* file = fopen(filepath.c_str(), "rb");
  if (file == nullptr) {
    std::cerr << "Error: cannot open file " << filepath << std::endl;
    return;
  }
  fread(array, sizeof(float), size, file);
  fclose(file);
}

void matmul(const float *A, const float *B, float *C, int M, int K, int N) {
  for (int row = 0; row < M; row++) {
    for (int col = 0; col < N; col++) {
      float sum = 0.0;
      for (int i = 0; i < K; i++) {
        sum += A[row * K + i] * B[i * K + col];
      }
      C[row * N + col] = sum;
    }
  }
}

void reorder_matmul(const float *A, const float *B, float *C, int M, int K, int N) {
  for (int row = 0; row < M; row++) {
    for (int i = 0; i < K; i++) {
      for (int col = 0; col < N; col++) {
        C[row * N + col] += A[row * K + i] * B[i * N + col];
      }
    }
  }
}

bool assert_array_equal(const float *A, const float *B, int size) {
  float epsilon = 1e-3;

  for (int i = 0; i < size; i++) {
    if (auto diff = std::fabs(A[i] - B[i]); diff > epsilon) {
      std::cerr << "Error: A[" << i << "] != B[" << i << "] (" << A[i] << " != " << B[i] << "), diff = " << diff << std::endl;
      return false;
    }
  }
  return true;
}

int main() {
  float *A = new float[N * N];
  float *B = new float[N * N];
  float *C = new float[N * N];
  float *ret = new float[N * N];

  load_float32_array("../A_1024.mat", A, N * N);
  load_float32_array("../B_1024.mat", B, N * N);
  load_float32_array("../C_1024.mat", C, N * N);

  auto start = std::chrono::high_resolution_clock::now();
  reorder_matmul(A, B, ret, N, N, N);
  auto end = std::chrono::high_resolution_clock::now();

  auto speed_info = get_speed_information(N, N, N, start, end);
  std::cout << "GFLOPs for " << N << "x" << N << " matrix multiplication = " << speed_info.FLOPs << " GFLOPs" << std::endl;
  // TODO: elapse should be in micro seconds
  std::cout << "Elapsed " << speed_info.elapsed << " seconds, FLOPS = " << std::fixed << std::setprecision(5) << speed_info.FLOPS << " GFLOPS" << std::endl;

  if (assert_array_equal(C, ret, N * N)) {
    std::cout << "Success: C == A * B" << std::endl;
  } else {
    std::cerr << "Error: C != A * B" << std::endl;
  }

  return 0;
}
