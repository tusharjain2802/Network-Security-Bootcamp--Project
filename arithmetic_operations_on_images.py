import cv2 
import numpy as np

image1=cv2.imread("download.jpg")
image2=cv2.imread("download1.jpg")
image3=cv2.imread("download2.jpg")
image5=np.ones(image1.shape,np.uint8)
#ones means a plane white image will be formed.
#size of image5 should be the same to image1 to apply filter on it
image5 = image5*100
#image4 = image3*2
#all the pixels get doubled
image4=cv2.add(image1,image5)
#this adds image1 and image5 and makes it brighter.
image2=cv2.resize(image2,(1041,585))
image6=cv2.add(image2,image1)
cv2.imshow("frame1",image1)
cv2.imshow("frame2",image2)
cv2.imshow("frame3",image3)
cv2.imshow("frame4",image4)
cv2.imshow("frame5",image6)

cv2.waitKey()
cv2.destroyAllWindows()
