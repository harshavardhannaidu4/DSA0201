import cv2
img = cv2.imread("input.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobel_y = cv2.Sobel(
    gray,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)
sobel_y = cv2.convertScaleAbs(sobel_y)
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y", sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
