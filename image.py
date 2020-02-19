import cv2
import numpy as np
img = cv2.imread('lenna.jpg')
img1 = cv2.imread('dog.jpg')
# ROI截取
#face = img[123:239, 145:216]
face = img1[162:278, 190:261]
cv2.imshow('face', face)
img[123:239, 145:216] = face
eyes = img[154:172, 154:220]
cv2.imshow('eyes', eyes)
cv2.imshow('tpe101',img1)
cv2.imshow('Lenna',img)
cv2.waitKey(0)