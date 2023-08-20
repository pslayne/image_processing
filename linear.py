import numpy as np
import cv2 as cv

def inverse(img):
  return 1 - img

def interval(img, g_min, g_max):
  gray_channel = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  img = np.dstack((gray_channel, gray_channel, gray_channel))
  f_min = min(img.flatten())
  f_max = max(img.flatten())

  g = (g_max - g_min) / (f_max - f_min)

  new_img = []
  for line in img:
    aux = []
    for px in line:
      aux.append(g * (px - f_min) + g_min)
    new_img.append(aux)

  return np.array(new_img)

def binary(img, t = 128):
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  _, t = cv.threshold(img, t, 255, cv.THRESH_BINARY)
  return t