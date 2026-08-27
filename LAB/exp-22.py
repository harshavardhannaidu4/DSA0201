import cv2

# Read input image
img = cv2.imread("input22.jpg")

if img is None:
    print("Image not found!")
    exit()

# Watermark text
text = "OPEN CV"

# Position of watermark
position = (30, 50)

# Font
font = cv2.FONT_HERSHEY_SIMPLEX

# Font size
font_scale = 1

# Color - White
color = (255, 255, 255)

# Thickness
thickness = 2

# Add watermark
cv2.putText(
    img,
    text,
    position,
    font,
    font_scale,
    color,
    thickness,
    cv2.LINE_AA
)

# Display
cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
