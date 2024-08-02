import numpy as np
from scipy.ndimage import rotate

def make_rotate_degree(degree: float) -> np.ndarray:
    # Your code here
    rotated_array = rotate(input_array, angle=degree)
    return rotated_array
