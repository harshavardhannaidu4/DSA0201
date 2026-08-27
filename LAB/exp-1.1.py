import cv2
a=cv2.imread("image.jpg")
gray=cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",a)
cv2.imshow("Gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()