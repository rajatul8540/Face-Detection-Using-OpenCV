import cv2

video_cap = cv2.VideoCapture(0)

if not video_cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

while True:
    ret, video_data = video_cap.read()

    if ret:
        cv2.imshow("video_live", video_data)

    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()
cv2.destroyAllWindows()
