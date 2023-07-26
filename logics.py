import cv2 as cv
import numpy as np

def logical_and(img_a, img_b):
    img_and = cv.bitwise_and(img_a, img_b)
    return img_and

def logical_or(img_a, img_b):
    img_or = cv.bitwise_or(img_a, img_b)
    return img_or

def logical_xor(img_a, img_b):
    img_xor = cv.bitwise_xor(img_a, img_b)
    return img_xor

