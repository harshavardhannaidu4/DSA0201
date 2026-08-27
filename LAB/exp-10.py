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
    [w, 30],
    [w - 30, h],
    [30, h - 30]
])
H, status = cv2.findHomography(src, dst)
print("Homography Matrix:")
print(H)
result = cv2.warpPerspective(img, H, (w, h))
cv2.imshow("Original", img)
cv2.imshow("Homography Transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
