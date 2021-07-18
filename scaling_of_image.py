import cv2 
import numpy as np

image1= cv2.imread("download.jpg")

image2= cv2.resize(image1,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
cv2.imshow("Linear",image2)
image2= cv2.resize(image1,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_AREA)
cv2.imshow("area",image2)
image2= cv2.resize(image1,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_NEAREST)
cv2.imshow("nearest",image2)
image2= cv2.resize(image1,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
cv2.imshow("cubic",image2)
image2= cv2.resize(image1,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Lanczos4",image2)

cv2.imshow("original",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()