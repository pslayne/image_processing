import numpy as np

def norm_color(img):
  max, min = max_min_color(img)
  new_img = []
  for line in img:
    aux_line = []
    for pixel in line:
      aux_pixel = []
      for i in range(3):
        # if pixel[i] < 0 or pixel[i] > 255:
        #   new_color = round((255 / (max[i] - min[i])) * (pixel[i] - min[i]))
        #   aux_pixel.append(new_color)
        if pixel[i] < 0:
          aux_pixel.append(0)
        elif pixel[i] > 255:
          aux_pixel.append(255)
        else:
          aux_pixel.append(round(pixel[i]))
      aux_line.append(aux_pixel)
    new_img.append(aux_line)

  return np.array(new_img)

def max_min_color(img):
  red = []
  green = []
  blue = []

  for line in img:
    for pixel in line:
      red.append(pixel[0])
      green.append(pixel[1])
      blue.append(pixel[2])

  max_img = [max(red),
             max(green),
             max(blue)]

  min_img = [min(red),
             min(green),
             min(blue)]

  return max_img, min_img