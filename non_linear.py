import numpy as np
import cv2 as cv

def log(img):
  img = img.astype(np.int32)
  c = 255 / (np.log(1 + np.max(img)))
  log_transformed = np.array(c * np.log(1 + img), dtype = np.int32)
  return log_transformed


def root(img):
  img = img.astype(np.int32)
  square = np.sqrt(img)
  return square

def exp(img, b = 10):
  # valor de saída = fator de escala * (base ^ valor de entrada - 1)
  img = img.astype(np.complex128)
  exponencial = np.power(b, img)
  return exponencial

def squared(img):
  img = img.astype(np.int32)
  return np.square(img)
