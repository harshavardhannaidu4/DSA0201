import cv2
import numpy as np
img = cv2.imread("input.png")
tx = 100   
ty = 50    
M = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])
result = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
