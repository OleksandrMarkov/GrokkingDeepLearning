import cv2

img = cv2.imread("dataset/photos/stephen McDaniel3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

FACE_RECOG_MODEL = "model/faces.xml"
face_cascade = cv2.CascadeClassifier(FACE_RECOG_MODEL)
faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)
for (x, y, w, h) in faces:
	#img = img[x:y+h]
    img = img[y:y + h, x:x + w]
    way_to_cropped_img = f"dataset/photos/stefgdgjlfdjdphenMfgfcDaniel3.jpg"        
    cv2.imwrite(way_to_cropped_img, img)

print("!!!")