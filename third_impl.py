import cv2 as cv
from colors import color_component

img = cv.imread('images/lena_cor.jpg')
cv.imshow("Source", img)
cv.waitKey(0)

red = color_component(img, 'r')
cv.imshow("Red Channel", red)
cv.waitKey(0)

green = color_component(img, 'g')
cv.imshow("Green Channel", green)
cv.waitKey(0)

blue = color_component(img, 'b')
cv.imshow("Blue Channel", blue)
cv.waitKey(0)

cv.destroyAllWindows()