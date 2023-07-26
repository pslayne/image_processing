import cv2 as cv
import numpy as np
from arithmetics import add, sub, mult, div
from logics import logical_and, logical_or, logical_xor
from structure import resize
import math

# img_a = cv.imread('images/lena.pgm', -1)
# img_b = cv.imread('images/Airplane.pgm', -1)

#precisa do resize
img_a = cv.imread('images/tricolor_cat.jpg')
# img_b = cv.imread('images/lena_cor.jpg')
img_b = cv.imread('images/orange_cat.jpg')

#############################
#     ajuste de tamanho     #
#############################

img_a, img_b = resize(img_a, img_b)

print(img_a.shape, img_b.shape)

cv.imshow("A", img_a)
k = cv.waitKey(0)

cv.imshow("B", img_b)
k = cv.waitKey(0)


#############################
#   operações aritméticas   #
#############################

img_add = add(img_a, img_b)
cv.imshow("Adicao", img_add)
k = cv.waitKey(0)

img_sub = sub(img_a, img_b)
cv.imshow("Subtracao", img_sub)
k = cv.waitKey(0)

img_mult = mult(img_a, img_b)
cv.imshow("Multiplicacao", img_mult)
k = cv.waitKey(0)

img_div = div(img_a, img_b)
cv.imshow("Divisao", img_div)
k = cv.waitKey(0)

#############################
#     operações lógicas     #
#############################

img_and = logical_and(img_a, img_b)
cv.imshow("AND", img_and)
k = cv.waitKey(0)

img_or = logical_or(img_a, img_b)
cv.imshow("OR", img_or)
k = cv.waitKey(0)

img_xor = logical_xor(img_a, img_b)
cv.imshow("XOR", img_xor)
k = cv.waitKey(0)

cv.destroyAllWindows()



