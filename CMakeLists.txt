cmake_minimum_required(VERSION 3.17)
project(ctypes_example)

set(CMAKE_CXX_STANDARD 20)

add_library(
        adder SHARED
        adder/adder.cpp
        adder/adder.h
)

