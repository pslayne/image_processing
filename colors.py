import cv2 as cv
import numpy as np

# separação de canais
def split_components(img, channel):
    ############################################
    #                    RGB                   #
    ############################################
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

    ############################################
    #                    HSV                   #
    ############################################
    if channel == 'h':
        return img[:,:,0]

    if channel == 's':
        return img[:,:,1]

    if channel == 'v':
        return img[:,:,2]

    ############################################
    #                    YUV                   #
    ############################################
    if channel == 'yu':
      yu = np.zeros(img.shape)
      yu[:,:,0] = img[:,:,0]
      yu[:,:,1] = img[:,:,1]
      return yu

    if channel == 'yv':
      yv = np.zeros(img.shape)
      yv[:,:,0] = img[:,:,0]
      yv[:,:,2] = img[:,:,2]
      return yv

    ############################################
    #                   CMYK                   #
    ############################################
    if channel == 'c':
        cyan_channel = img[:,:,0]
        cyan_img = np.zeros(img.shape)
        cyan_img[:,:,0] = cyan_channel
        return cmy2rgb(cyan_img)

    if channel == 'm':
        magenta_channel = img[:,:,1]
        magenta_img = np.zeros(img.shape)
        magenta_img[:,:,1] = magenta_channel
        return cmy2rgb(magenta_img)

    if channel == 'y':
        yellow_channel = img[:,:,2]
        yellow_img = np.zeros(img.shape)
        yellow_img[:,:,2] = yellow_channel
        return cmy2rgb(yellow_img)

    if channel == 'k':
        key_channel = img[:,:,3]
        key_img = (np.dstack((key_channel, key_channel, key_channel))).astype(np.uint8)
        return key_img

def convert_from_rgb(img, space):
  if space == 'hsv':
    return cv.cvtColor(img, cv.COLOR_BGR2HSV);
  if space == 'yuv':
    return cv.cvtColor(img, cv.COLOR_BGR2YUV);
  if space == 'cmy':
    return rgb2cmy(img);
  if space == 'cmyk':
    return rgb2cmyk(img);

def rgb2cmy(image):
  img = image.astype(np.float64)/255.
  C = 1-img[...,2]
  M = 1-img[...,1]
  Y = 1-img[...,0]

  cmy_image = (np.dstack((C,M,Y)) * 255).astype(np.uint8)
  return cmy_image

def cmy2rgb(image):
  img = image.astype(np.float64)/255.
  B = 1-img[...,2]
  G = 1-img[...,1]
  R = 1-img[...,0]

  cmy_image = (np.dstack((B, G, R)) * 255).astype(np.uint8)
  return cmy_image

def rgb2cmyk(image):
  # Make float and divide by 255 to give BGRdash
  bgrdash = image.astype(np.float64)/255.

  # Calculate K as (1 - whatever is biggest out of Rdash, Gdash, Bdash)
  K = 1 - np.max(bgrdash, axis=2)

  # Calculate C
  C = (1-bgrdash[...,2] - K)/(1-K)

  # Calculate M
  M = (1-bgrdash[...,1] - K)/(1-K)

  # Calculate Y
  Y = (1-bgrdash[...,0] - K)/(1-K)

  # Combine 4 channels into single image and re-scale back up to uint8
  CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)
  return CMYK

