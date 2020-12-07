import ctypes
import numpy as np

lib: ctypes.CDLL = ctypes.cdll.LoadLibrary("./cmake-build-release/libadder.so")
lib.canvas_add.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_uint64]
lib.canvas_add.restype = ctypes.c_double

def canvas_add(canvas: np.ndarray, addon: np.ndarray) -> float:
    if not (canvas.flags.c_contiguous and addon.flags.c_contiguous):
        raise Exception("parameters must be contiguous")
    if not (canvas.dtype == np.float64 and addon.dtype == np.float64):
        raise Exception("parameters must be np.float64")

    c_count: ctypes.c_uint64 = ctypes.c_uint64(addon.size)
    c_canvas: ctypes.POINTER(ctypes.c_double) = canvas.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    c_addon: ctypes.POINTER(ctypes.c_double) = addon.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    c_sum: ctypes.c_double = lib.canvas_add(c_canvas, c_addon, c_count)
    return float(c_sum)
