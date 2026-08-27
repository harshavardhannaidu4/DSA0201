import numpy as np
import cv2

# Input image as a matrix
img = np.array([
    [10, 10, 10, 10, 10],
    [10, 20, 20, 20, 10],
    [10, 20, 50, 20, 10],
    [10, 20, 20, 20, 10],
    [10, 10, 10, 10, 10]
], dtype=np.float32)

# Laplacian mask with negative center coefficient
mask = np.array([
    [0,  1, 0],
    [1, -4, 1],
    [0,  1, 0]
], dtype=np.float32)

# Apply convolution
laplacian = cv2.filter2D(img, -1, mask)

# Sharpening: original - Laplacian
sharpened = img - laplacian

# Display matrices
print("Original Image:")
print(img)

print("\nLaplacian:")
print(laplacian)

print("\nSharpened Image:")
print(sharpened)
