import cv2 

image= cv2.VideoCapture(0)
count=0
while(True):
	count+=1
	check,frame= image.read()

	cv2.imshow("my image",frame)
	if cv2.waitKey() == ord('q'):
		break

	print(frame.shape)

	cv2.imwrite("my image"+str(count)+".jpg",frame)
image.release()
cv2.destroyAllWindows()