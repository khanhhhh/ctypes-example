cmake_minimum_required(VERSION 3.17)
project(ctypes_example)

set(CMAKE_CXX_STANDARD 20)

add_library(
        adder SHARED
        adder/core/adder.cpp
        adder/core/adder.h
        adder/wrapper/adder_wrapper.cpp
        adder/wrapper/adder_wrapper.h
)

