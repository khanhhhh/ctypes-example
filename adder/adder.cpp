#include "adder.h"

double canvas_add(double *canvas, double *addon, uint64_t count) {
    double sum = 0;
    for (uint64_t i = 0; i < count; i++) {
        canvas[i] += addon[i];
        sum += addon[i];
    }
    return sum;
}
