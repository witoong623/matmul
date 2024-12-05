cmake_minimum_required(VERSION 3.15...3.31)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -stdlib=libc++ -fuse-ld=lld-15")

project(matmul LANGUAGES CXX)

add_executable(matmul main.cpp)

target_compile_features(matmul PUBLIC cxx_std_20)
target_compile_options(matmul PRIVATE "-O3")
set_target_properties(matmul PROPERTIES CXX_EXTENSIONS OFF)
