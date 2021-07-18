import cv2 
import numpy as np

image1= cv2.imread("download.jpg")

row,col,ch=image1.shape 

R=cv2.getRotationMatrix2D((row/2,col/2),45,1)
#((center of roatation), angle of division, scaling factor)

image2= cv2.warpAffine(image1,R,(col,row))

cv2.imshow("frame1",image1)
cv2.imshow("frame2",image2)

k=cv2.waitKey(0)
cv2.destroyAllWindows()