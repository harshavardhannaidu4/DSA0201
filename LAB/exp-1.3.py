import cv2
c=cv2.imread("image.jpg")
edges=cv2.Canny(c,100,200)
cv2.imshow("Original",c)
cv2.imshow("Edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()