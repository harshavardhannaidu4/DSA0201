import cv2
import numpy as np
e=cv2.imread("image.jpg")
kernel=np.ones((5,5),np.uint8)
erode=cv2.erode(e,kernel,iterations=1)
cv2.imshow("Original",e)
cv2.imshow("Eroded",erode)
cv2.waitKey(0)
cv2.destroyAllWindows()