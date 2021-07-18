import cv2 
def mouse_event(event,x,y,flag,param):
	if (event==cv2.EVENT_x):
		cv2.putText(image,"Hello World",(x,y),cv2.FONT_ITALIC,1,(0,0,255),3)
	cv2.imshow("Frame",image)

image=cv2.imread("download.jpg")

cv2.imshow("Frame",image)
cv2.setMouseCallback("Frame", mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()