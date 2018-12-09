import cv2

img=cv2.imread('square.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)

cv2.imwrite("thesh_square.jpg", thresh)


cv2.waitKey(0)
