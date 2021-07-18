import cv2 
import numpy as np

image1= cv2.imread("download.jpg")

kernal=np.array([[-1,-1,-1],
	[-1,9,-1],
	[-1,-1,-1]])

image2=cv2.filter2D(image1,-1,kernal)

cv2.imshow("original",image1)
cv2.imshow("filter",image2)
cv2.waitKey()
cv2.destroyAllWindows()