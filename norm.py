import numpy as np

def norm(img):
  print(img.dtype)
  max_img, min_img = max_min(img)
  new_img = []
  for line in img:
    aux_line = []
    for pixel in line:
      aux_pixel = []
      for i in range(3):
        if pixel[i] < 0 or pixel[i] > 255:
          new_pixel = np.round((255 / (max_img[i] - min_img[i])) * (pixel[i] - min[i]))
          aux_pixel.append(new_pixel)
        else:
          aux_pixel.append(np.round(pixel[i]))
      aux_line.append(aux_pixel)
    new_img.append(aux_line)

  new_img = np.array(new_img, dtype=img.dtype)
  print(new_img.dtype)
  return new_img

def trunc(img):
  shape = img.shape
  img = img.flatten()
  trunc = []
  for px in img:
    if px > 255:
      trunc.append(255)
    elif px < 0:
      trunc.append(0)
    else:
      trunc.append(px)
  trunc = np.array(trunc, np.int32)
  return np.reshape(trunc, shape)

def max_min(img):
  red = img[:,:,2].flatten()
  green = img[:,:,1].flatten()
  blue = img[:,:,0].flatten()

  max_img = [max(red),
             max(green),
             max(blue)]

  min_img = [min(red),
             min(green),
             min(blue)]

  return max_img, min_img