import cv2
import time
modes = [
    ("Normal Speed", 30, 5),
    ("Slow Motion", 100, 5),
    ("Fast Motion", 1, 5)
]
for title, delay, duration in modes:
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if title == "Fast Motion":
            cap.read()
        cv2.imshow(title, frame)
        if time.time() - start_time > duration:
            break
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

    cap.release()
    cv2.destroyAllWindows()
print("Webcam video processing completed.")
