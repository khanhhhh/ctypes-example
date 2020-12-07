import numpy as np

import adder


def main():
    canvas: np.ndarray = np.random.random(5).astype(np.float64)
    addon: np.ndarray = np.random.random(2).astype(np.float64)
    print(canvas)
    print(addon)
    print(adder.canvas_add(canvas, addon))
    print(canvas)


if __name__ == "__main__":
    main()
