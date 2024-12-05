## Speed of matmul
CPU is i7-9700K at 3.6 GHz. Matrix size is 1024x1024.

| Matmul variant | Speed (FLOPS) |
| -------------- | ------------- |
| Naive          | 0.7           |


## Note on how to install clang in Ubuntu 22.04
1. Install tools. In this case, I use clang 15, which isn't the default version for Ubuntu 22.04 (default is 14).
    - clang-15
    - libc++-15-dev
    - libc++abi-15-dev
    - lld-15
2. To make CMake extension and terminal work in VS Code, set the config for the extension at least as follow.
```
{
    "cmake.configureEnvironment": {
        "CC": "/usr/bin/clang-15",
        "CXX": "/usr/bin/clang++-15"
    },
    "cmake.buildEnvironment": {
        "CC": "/usr/bin/clang-15",
        "CXX": "/usr/bin/clang++-15"
    },
    "terminal.integrated.env.linux": {
        "CC": "/usr/bin/clang-15",
        "CXX": "/usr/bin/clang++-15"
    }
}
```
3. Set the `C` and `CXX` environment variable to clang and clang++ to be able to run cmake in terminal outside VS Code. (Probably the better way to do this is to use update-alternatives to set the default version of clang command to version 15.)
```
export CC=/usr/bin/clang-15
export CXX=/usr/bin/clang++-15
```
4. Set compiler flag in CMakeLists.txt `set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++")`.
    This will tell it to use libc++ as standard lib.
5. Set linker flag in CMakeLists.txt as follow `set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -stdlib=libc++ -fuse-ld=lld-15")`.
    This will tell it to use libc++, c++abi and lld as linker.
6. Run `clang++ -v -E` to find out what g++ version does clang++ look for library, install the corresponding `libstdc++-dev`.

#### Resource
https://stackoverflow.com/questions/7031126/switching-between-gcc-and-clang-llvm-using-cmake  
https://stackoverflow.com/questions/27178106/linking-libc-to-cmake-project-on-linux  
https://askubuntu.com/questions/1449769/clang-cannot-find-iostream  
