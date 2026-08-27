import cv2
import numpy as np
img = cv2.imread("input.png")
h, w = img.shape[:2]
src = np.float32([
    [50, 50],
    [w - 50, 50],
    [w - 50, h - 50],
    [50, h - 50]
])
dst = np.float32([
    [0, 0],
    [w, 0],
    [w, h],
    [0, h]
])
M = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, M, (w, h))
cv2.imshow("Original", img)
cv2.imshow("Perspective Transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
