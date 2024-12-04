cmake_minimum_required(VERSION 3.15...3.31)

set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fuse-ld=lld")
project(matmul LANGUAGES CXX)

add_executable(matmul main.cpp)
