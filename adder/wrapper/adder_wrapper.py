import ctypes

import numpy as np


lib: ctypes.CDLL = ctypes.cdll.LoadLibrary("./cmake-build-release/libadder.so")

def add(canvas: np.ndarray, addon: np.ndarray):
    if not (canvas.flags.c_contiguous and addon.flags.c_contiguous):
        raise Exception("parameters must be contiguous")
    if not (canvas.dtype == np.float64 and addon.dtype == np.float64):
        raise Exception("parameters must be np.float64")

    c_count: ctypes.c_uint64 = ctypes.c_uint64(addon.size)
    c_canvas: ctypes.POINTER(ctypes.c_double) = canvas.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    c_addon: ctypes.POINTER(ctypes.c_double) = addon.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    lib.c_canvas_add(c_canvas, c_addon, c_count)
