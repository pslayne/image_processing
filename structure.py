import cv2 as cv
from math import floor, ceil

def resize(img_a, img_b):
    if img_a.shape == img_b.shape:
        pass
    else:
        # shape[0] = x | shape[1] = y   
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
