import cv2 as cv
 # Reading Image
# 
image = cv.imread('1.jpg')
cv.imshow("Image Displayed", image)

# Reading Videos
# capture = cv.VideoCapture('2.mp4')

# while True:
# 	isTrue, frame = capture.read()
# 	cv.imshow("Video", frame)

# 	if cv.waitKey(20) & 0xFF==ord('d'):
# 		break

# capture.release()
# cv.destroyAllWindows()