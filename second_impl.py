import cv2 as cv
from geometrics import rotate, translate, scale, reflex, shear

img = cv.imread('images/orange_cat.jpg')
# img = cv.imread('images/lena.pgm')
cv.imshow("Source", img)
cv.waitKey(0)

cv.imshow("Rotate", rotate(img, 30))
cv.waitKey(0)

cv.imshow("Translate", translate(img, 30, 50))
cv.waitKey(0)

cv.imshow("Scale up", scale(img, 30))
cv.waitKey(0)

cv.imshow("Scale down", scale(img, 30, 'down'))
cv.waitKey(0)

cv.imshow("Reflex X", reflex(img, 0))
cv.waitKey(0)

cv.imshow("Reflex Y", reflex(img, 1))
cv.waitKey(0)

cv.imshow("Reflex both", reflex(img, -1))
cv.waitKey(0)

cv.imshow("Shear", shear(img, -1, 50))
cv.waitKey(0)

cv.destroyAllWindows()
