import cv2
import numpy as np

# Read input image
img = cv2.imread("input19.jpg")

if img is None:
    print("Image not found!")
    exit()

# Convert image to float
img_float = img.astype(np.float32)

# Create blurred image
blurred = cv2.GaussianBlur(img_float, (5, 5), 0)

# Create unsharp mask
unsharp_mask = img_float - blurred

# Sharpened image
sharpened = img_float + unsharp_mask

# Convert values to 0-255
sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

# Convert unsharp mask for display
unsharp_display = np.clip(
    np.abs(unsharp_mask),
    0,
    255
).astype(np.uint8)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blurred.astype(np.uint8))
cv2.imshow("Unsharp Mask", unsharp_display)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
