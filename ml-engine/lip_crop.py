import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def crop_lip_region(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Approximate lower half of face as lip region
        lip_y = y + int(0.6 * h)
        lip_h = int(0.3 * h)
        lip = frame[lip_y:lip_y+lip_h, x:x+w]
        return lip

    return None
