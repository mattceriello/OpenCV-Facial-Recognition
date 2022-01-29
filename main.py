import cv2, time
faceCascade = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
time.sleep(1)
while True:
    img = cap.read()[1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break