import cv2 
import numpy as np

image1= cv2.imread("download.jpg")

row,col,ch=image1.shape 

x=0
y=0

while(True):

	T=np.float64([[1,0,x],[0,1,y]])

	image2=cv2.warpAffine(image1,T,(col,row))

	cv2.imshow("frame1",image1)
	cv2.imshow("frame2",image2)
	k=cv2.waitKey(1)
	if k==ord('q'):
		break
	x=x+1
	y=y+1
cv2.destroyAllWindows()