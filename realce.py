import cv2 as cv
import numpy as np
from arithmetics import binary

def adjust_gamma(image, gamma=1.0):
  # lookup table mapeando os valores [0, 255] pros valores de gamma ajustados
  inv_gamma = 1.0 / gamma
  table = np.array([((i / 255.0) ** inv_gamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

  # aplica a correção gamma usando a lut
  return cv.LUT(image, table)

def bit_plane(img, n = 0):
  if img.shape[2] >= 3:
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  bitmap = []
  for line in img:
    bits = [ int(binary(px)[n]) for px in line ]
    show_mode = [ ( 255 if b == 1 else 0 ) for b in bits]
    bitmap.append(show_mode)
  return np.array(bitmap)
