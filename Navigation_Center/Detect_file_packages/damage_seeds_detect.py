
import numpy as np
import cv2 as cv
import os

def damege_seeds_detect(img):

    min = np.array([0, 94, 0])
    max = np.array([21, 255, 255])

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, min, max)
    canny = cv.Canny(mask, 60, 165, 3)
    dilate = cv.dilate(canny, (10, 10), iterations=2)

    ret, thresh = cv.threshold(mask, 127, 255, cv.THRESH_BINARY_INV)

    # remove damege seeds out img
    bitwise = cv.bitwise_or(img, img, mask=thresh)

    contours, hierarchies = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    final = cv.drawContours(img.copy(), contours, -1, (0, 0, 255), 2)



    return final,contours

