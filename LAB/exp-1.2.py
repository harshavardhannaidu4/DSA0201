import cv2
b= cv2.imread("image.jpg")
blur= cv2.GaussianBlur(b,(7,7),0)
cv2.imshow("Original",b)
cv2.imshow("Blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
