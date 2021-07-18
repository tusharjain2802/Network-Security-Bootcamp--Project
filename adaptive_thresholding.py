import cv2 

image1= cv2.imread("download.jpg")
image1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)

#ret,image2=cv2.threshold(image1,140,225,cv2.THRESH_BINARY)
image2=cv2.adaptiveThreshold(image1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5)
image3=cv2.adaptiveThreshold(image1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN,cv2.THRESH_BINARY,5,5)

cv2.imshow("original",image1)
cv2.imshow("Mean",image2)
cv2.imshow("Gaussian",image3)
cv2.waitKey()
cv2.destroyAllWindows()