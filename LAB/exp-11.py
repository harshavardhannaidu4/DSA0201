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
A = []

for (x, y), (u, v) in zip(src, dst):
    A.append([-x, -y, -1, 0, 0, 0, x*u, y*u, u])
    A.append([0, 0, 0, -x, -y, -1, x*v, y*v, v])
A = np.array(A)
U, S, Vt = np.linalg.svd(A)
H = Vt[-1].reshape(3, 3)
H = H / H[2, 2]
print("Homography Matrix using DLT:")
print(H)
result = cv2.warpPerspective(img, H, (w, h))
cv2.imshow("Original", img)
cv2.imshow("DLT Transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
