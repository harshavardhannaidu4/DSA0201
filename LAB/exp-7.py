import cv2
import numpy as np
img = cv2.imread("input.png")
h, w = img.shape[:2]
src = np.float32([
    [0, 0],
    [w - 1, 0],
    [0, h - 1]
])
dst = np.float32([
    [50, 50],
    [w - 100, 80],
    [80, h - 50]
])
M = cv2.getAffineTransform(src, dst)
result = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Original", img)
cv2.imshow("Affine Transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
