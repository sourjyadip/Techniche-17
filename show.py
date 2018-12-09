import cv2
import numpy as np 

img=cv2.imread("opencv_frame_0.png")
crop_img = img[0:480, 80:560]
res = cv2.resize(img,(64,64), interpolation = cv2.INTER_CUBIC)
s=np.shape(res)
cv2.imshow("original",img)
cv2.imshow("cropped", crop_img)
cv2.imshow("resized",res)


height=np.size(img,0)
width=np.size(img,1)
print height
print width
cv2.waitKey(0)
cv2.destroyAllWindows()