import cv2 as cv


# rescale and resize a video and image frame

def rescaleFrame(frame, scale = 0.75):
	width = int(frame.shape[0] * scale) # width of the image
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)	

# reading images
# img = cv.imread('1.jpg')
# cv.imshow('Disha', img)
# cv.waitKey(0)

# reading videos
capture = cv.VideoCapture('2.mp4')

while True:
	isTrue, frame = capture.read()
	frame_resized = rescaleFrame(frame, scale = 0.2)

	cv.imshow("Video", frame)
	cv.imshow("Video Resized", frame_resized)
	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv.destroyAllWindows()

