import cv2
import numpy

cap = cv2.VideoCapture(1)

while True:
	ret,cam = cap.read()
	cv2.imshow("",cam)
	if cv2.waitKey(5) == 27:
		break
cv2.destroyAllWindows()
cap.release() 
