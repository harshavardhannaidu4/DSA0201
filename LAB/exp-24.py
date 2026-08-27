import cv2
import numpy as np

# Read input image
img = cv2.imread("input24.jpg", 0)

if img is None:
    print("Image not found!")
    exit()

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion = cv2.erode(
    img,
    kernel,
    iterations=1
)

# Display original image
cv2.imshow("Original Image", img)

# Display eroded image
cv2.imshow("Eroded Image", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
