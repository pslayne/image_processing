import cv2 as cv
import numpy as np

def color_component(img, channel):
    # BGR color space
    if channel == 'r':
        red_channel = img[:,:,2]
        red_img = np.zeros(img.shape)
        red_img[:,:,2] = red_channel
        return red_img
    if channel == 'g':
        green_channel = img[:,:,1]
        green_img = np.zeros(img.shape)
        green_img[:,:,1] = green_channel
        return green_img
    if channel == 'b':
        blue_channel = img[:,:,0]
        blue_img = np.zeros(img.shape)
        blue_img[:,:,0] = blue_channel
        return blue_img
