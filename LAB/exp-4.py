import cv2
image_path = r'C:/Users/karan/OneDrive/Desktop/OPEN CV/lab cv.jpg'

img = cv2.imread(image_path)

if img is None:
    print("Unable to read image.")
    exit()

bigger = cv2.resize(img, None, fx=2, fy=2)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.imshow("Original", img)
cv2.imshow("Bigger", bigger)
cv2.imshow("Smaller", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
