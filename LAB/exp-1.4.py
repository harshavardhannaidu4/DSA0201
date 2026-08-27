import cv2
import numpy as np
d=cv2.imread("image.jpg")
kernel=np.ones((5,5),np.uint8)
dilate=cv2.dilate(d,kernel,iterations=1)
cv2.imshow("Original",d)
cv2.imshow("Dilated", dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()