import cv2 as cv 
import numpy as np

blank = np.zeros((500,500, 3), dtype = 'uint8')
img = cv.imread('1.jpg')


# paint the image a certain color
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Green', blank)

# draw a rectangle
# cv.rectangle(name of image, (position of the rectangle), (dimentions of the rectangle), (color), (thickness or borders))
# cv.rectangle(blank, (50,50), (250,250), (0,255,0), thickness = 2) # thickness = -1 or cv.filled(for filled rectangle)
# instead of 250, 250 it can be blank.shape[1]//2 and blank.shape[0]//2 for half dimensions



# draw a circle
# cv.circle(name of image, (position), radius, (color), (thickness))
# cv.circle(blank, (250, 250), 40, (0,0,255), thickness = 3 )


# draw a line
# cv.line(name of image, (starting), (ending), (color), (thickness))
# cv.line(blank, (100,100),(250, 250), (0, 255, 0), thickness = 3)

# write text
# cv.putText(name of image, (starting position), font, font scale, color, thickness)
cv.putText(blank, 'Hello Disha', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 2)
cv.imshow('Text', blank)


cv.waitKey(0)