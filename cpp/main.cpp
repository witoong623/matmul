#include <iostream>
#include <string>


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

int main() {
  float *A = new float[N * N];
  float *B = new float[N * N];
  float *C = new float[N * N];

  load_float32_array("../A_1024.mat", A, N * N);
  load_float32_array("../A_1024.mat", B, N * N);
  load_float32_array("../A_1024.mat", C, N * N);

  return 0;
}
