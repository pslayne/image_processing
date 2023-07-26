import cv2 as cv
import numpy as np

def add(img_a, img_b):
    img_add = cv.add(img_a, img_b) # trunca automaticamente
    #cv.imwrite("results/add.pgm", img_add)
    return img_add

def sub(img_a, img_b):
    img_sub = cv.subtract(img_a, img_b)
    return img_sub

def mult(img_a, img_b):
    img_mult = cv.multiply(img_a, img_b)
    return img_mult

def div(img_a, img_b):
    img_div = cv.divide(img_a, img_b)
    return img_div