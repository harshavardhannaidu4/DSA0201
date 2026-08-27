import cv2
import numpy as np

# Read input image
img = cv2.imread("input20.jpg")

if img is None:
    print("Image not found!")
    exit()

# Convert image to float
img_float = img.astype(np.float32)

# High-Boost constant
A = 2

# High-Boost mask
mask = np.array([
    [0, -1, 0],
    [-1, A + 4, -1],
    [0, -1, 0]
], dtype=np.float32)

# Apply high-boost mask
sharpened = cv2.filter2D(
    img_float,
    cv2.CV_32F,
    mask
)

# Keep pixel values between 0 and 255
sharpened = np.clip(
    sharpened,
    0,
    255
).astype(np.uint8)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("High Boost Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
