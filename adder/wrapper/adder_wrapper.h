//
// Created by khanh on 8/12/20.
//

#ifndef CTYPES_EXAMPLE_ADDER_WRAPPER_H
#define CTYPES_EXAMPLE_ADDER_WRAPPER_H
#ifdef __cplusplus
#include <cstdint>
#else
#include <stdint.h>
#endif


#ifdef __cplusplus
extern "C" {
#endif

    void c_canvas_add(double* canvas, double* addon, uint64_t count);

#ifdef __cplusplus
};
#endif
#endif //CTYPES_EXAMPLE_ADDER_WRAPPER_H
