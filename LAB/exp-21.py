import cv2
import numpy as np

# Read input image
img = cv2.imread("input21.jpg")

if img is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to float
gray_float = gray.astype(np.float32)

# Horizontal gradient mask
Gx = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float32)

# Vertical gradient mask
Gy = np.array([
    [-1,  0,  1],
    [-2,  0,  2],
    [-1,  0,  1]
], dtype=np.float32)

# Apply horizontal mask
gx = cv2.filter2D(
    gray_float,
    cv2.CV_32F,
    Gx
)

# Apply vertical mask
gy = cv2.filter2D(
    gray_float,
    cv2.CV_32F,
    Gy
)

# Calculate gradient magnitude
gradient = cv2.magnitude(gx, gy)

# Normalize gradient to 0-255
gradient = cv2.normalize(
    gradient,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

# Gradient masking / sharpening
sharpened = gray_float + gradient

# Keep values between 0 and 255
sharpened = np.clip(
    sharpened,
    0,
    255
).astype(np.uint8)

# Convert gradient for display
gradient_display = gradient.astype(np.uint8)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Gradient Image", gradient_display)
cv2.imshow("Gradient Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
