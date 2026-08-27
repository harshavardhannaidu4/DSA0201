import cv2
import numpy as np

# Input image matrix
img = np.array([
    [10, 10, 10, 10, 10],
    [10, 20, 20, 20, 10],
    [10, 20, 50, 20, 10],
    [10, 20, 20, 20, 10],
    [10, 10, 10, 10, 10]
], dtype=np.float32)

# Laplacian mask with diagonal neighbors
mask = np.array([
    [1,  1, 1],
    [1, -8, 1],
    [1,  1, 1]
], dtype=np.float32)

# Apply Laplacian mask
laplacian = cv2.filter2D(
    img,
    cv2.CV_32F,
    mask,
    borderType=cv2.BORDER_CONSTANT
)

# Sharpening
sharp = img - laplacian

# Limit values to 0-255
sharp = np.clip(sharp, 0, 255)

# Display matrices
print("Original Matrix:")
print(img.astype(int))

print("\nLaplacian Matrix:")
print(laplacian.astype(int))

print("\nSharpened Matrix:")
print(sharp.astype(int))

# Convert to uint8 for displaying
original_display = img.astype(np.uint8)
sharp_display = sharp.astype(np.uint8)

# Enlarge the 5x5 matrix for visualization
original_display = cv2.resize(
    original_display,
    (500, 500),
    interpolation=cv2.INTER_NEAREST
)

sharp_display = cv2.resize(
    sharp_display,
    (500, 500),
    interpolation=cv2.INTER_NEAREST
)

cv2.imshow("Original", original_display)
cv2.imshow("Laplacian Sharpened", sharp_display)

cv2.waitKey(0)
cv2.destroyAllWindows()
