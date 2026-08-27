import cv2
import numpy as np

# Read input image
img = cv2.imread("input23.jpg")

if img is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Boundary detection convolution kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
], dtype=np.float32)

# Apply convolution
boundary = cv2.filter2D(
    gray,
    cv2.CV_32F,
    kernel
)

# Convert negative values to positive
boundary = np.abs(boundary)

# Convert to 0-255
boundary = np.clip(
    boundary,
    0,
    255
).astype(np.uint8)

# Display original image
cv2.imshow("Original Image", gray)

# Display boundary
cv2.imshow("Boundary Image", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()
