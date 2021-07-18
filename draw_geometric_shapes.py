import cv2 
import numpy as np

img1= np.zeros((512,512,3),np.uint8)
#zeros gives blank black image

img=cv2.imread("download.jpg")
print(img.shape)

cv2.line(img,(10,10),(255,255),(56,255,0),5)
cv2.line(img1,(10,10),(255,255),(56,255,0),5)

cv2.arrowedLine(img,(50,10),(300,300),(56,255,0),5)
cv2.arrowedLine(img1,(50,10),(300,300),(56,255,0),5)

cv2.rectangle(img,(100,20),(200,40),(0,255,0),5)
cv2.rectangle(img1,(100,20),(200,40),(0,255,0),5)

cv2.circle(img,(255,255),100,(255,0,0),-1)
cv2.circle(img1,(255,255),100,(255,0,0),-1)
#255 is center of the page

cv2.putText(img,"shapes",(100,200),cv2.FONT_ITALIC,3,(0,0,255),5)
cv2.putText(img1,"shapes",(100,200),cv2.FONT_ITALIC,3,(0,0,255),5)

cv2.imshow("download_shape",img)
cv2.imshow("shape",img1)
cv2.waitKey()
cv2.destroyAllWindows()