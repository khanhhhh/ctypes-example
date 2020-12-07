#include "adder.h"

void canvas_add(double *canvas, double *addon, uint64_t count) {
    for (uint64_t i = 0; i < count; i++) {
        canvas[i] += addon[i];
    }
}
