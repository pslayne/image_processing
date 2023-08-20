import cv2 as cv
from math import floor, ceil, sin, cos
import numpy as np

def padding(img_a, img_b):
    if img_a.shape != img_b.shape:
        x = img_a.shape[0] - img_b.shape[0] # x > 0 : a > b | x < 0 : a < b
        if x > 0:
            img_b = cv.copyMakeBorder(img_b, floor(x/2), ceil(x/2), 0, 0, cv.BORDER_CONSTANT)
        else:
            x = -x
            img_a = cv.copyMakeBorder(img_a, floor(x/2), ceil(x/2), 0, 0, cv.BORDER_CONSTANT)

        y = img_a.shape[1] - img_b.shape[1] # y > 0 : a > b | y < 0 : a < b
        if y > 0:
            img_b = cv.copyMakeBorder(img_b, 0, 0, floor(y/2), ceil(y/2), cv.BORDER_CONSTANT)
        else:
            y = -y
            img_a = cv.copyMakeBorder(img_a, 0, 0, floor(y/2), ceil(y/2), cv.BORDER_CONSTANT)

    return img_a, img_b

def translate(img, d_x, d_y):
    M = np.float32([
        [1, 0, d_x], 
        [0, 1, d_y],
    ])
    t = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return t

def scale(img, rate, scale = 'up'):
    width = img.shape[1]
    height = img.shape[0]
    if scale == 'up':
        width = int(width * (rate / 100 + 1))
        height = int(height * (rate / 100 + 1))
    else: # scale down
        width = int(width * (1 - rate / 100))
        height = int(height * (1 - rate / 100))
    
    resized = cv.resize(img, (width, height), interpolation = cv.INTER_AREA)
    return resized

def rotate(img, rate):
    # calcula o centro
    (h, w) = img.shape[:2]
    (center_x, center_y) = (w // 2, h // 2)

    # gira a imagem em 'rate' graus
    M = cv.getRotationMatrix2D((center_x, center_y), rate, 1.0)

    img_rotate = cv.warpAffine(img, M, (w, h))

    return img_rotate

def reflex(img, axis): 
    # 0 = x | 1 = y | -1 = x e y
    return cv.flip(img, axis)

def shear(img, axis, rate):
    M2 = []
    if axis == 0 or axis == -1:
        M2 = np.float32([[1, rate/100, 0], [0, 1, 0]])
    if axis == 1 or axis == -1:
        M2 = np.float32([[1, 0, 0], [rate/100, 1, 0]])

    M2[0,2] = -M2[0,1] * img.shape[0]/2
    M2[1,2] = -M2[1,0] * img.shape[1]/2
    aff = cv.warpAffine(img, M2, (img.shape[0], img.shape[1]))
    return aff