## Note on how to install clang in Ubuntu 22.04
1. Install tools. Don't bother to install clang-15 (not the default one) because one of the tools we need don't have version 14 in Ubuntu repository yet
    - clang
    - lld
    - libc++abi-dev
2. To make CMake extension work in VS Code, set the config for the extension at least as follow.
```
{
    "cmake.configureEnvironment": {
        "CC": "/usr/bin/clang",
        "CXX": "/usr/bin/clang++"
    },
    "cmake.buildEnvironment": {
        "CC": "/usr/bin/clang",
        "CXX": "/usr/bin/clang++"
    }
}
```
3. Set the `C` and `CXX` environment variable to clang and clang++ to be able to run cmake in terminal.
4. Set linker flag in CMakeLists.txt as follow `set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fuse-ld=lld")`. This will tell it to use libc++, c++abi and lld as linker.
5. Run `clang++ -v -E` to find out what g++ version does clang++ look for library, install the corresponding `libstdc++-dev`.
