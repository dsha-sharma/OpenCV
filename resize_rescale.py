import cv2 as cv

def rescaleFrame(frame, scale = 0.5):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

#rescale video
# capture = cv.VideoCapture("2.mp4")
# while True:
# 	isTrue, frame = capture.read()
# 	frame_resized = rescaleFrame(frame, scale=0.5)
# 	cv.imshow("Video Resized",frame_resized)

# 	if cv.waitKey(20) & 0xFF==ord('d'):
# 		break

# capture.release()
# cv.destroyAllWindows()

#rescale images
image = cv.imread('1.jpg')
resized_image = rescaleFrame(image)
cv.imshow("Resized Image",resized_image)