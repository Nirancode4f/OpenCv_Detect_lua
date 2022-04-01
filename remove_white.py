

import cv2 as cv
import os
import numpy as np

def nothing(x):
    pass

cv.namedWindow("remmove_white")

cv.createTrackbar("min-H", "remmove_white", 0, 255, nothing)
cv.createTrackbar("min-S", "remmove_white", 0, 255, nothing)
cv.createTrackbar("min-V", "remmove_white", 0, 255, nothing)

cv.createTrackbar("max-H", "remmove_white", 201, 255, nothing)
cv.createTrackbar("max-S", "remmove_white", 57, 255, nothing)
cv.createTrackbar("max-V", "remmove_white", 255, 255, nothing)

def remove_white(img):

    minH = cv.getTrackbarPos("min-H", "remmove_white")
    minS = cv.getTrackbarPos("min-S", "remmove_white")
    minV = cv.getTrackbarPos("min-V", "remmove_white")
    maxH = cv.getTrackbarPos("max-H", "remmove_white")
    maxS = cv.getTrackbarPos("max-S", "remmove_white")
    maxV = cv.getTrackbarPos("max-V", "remmove_white")

    min = np.array([minH, minS, minV])
    max = np.array([maxH, maxS, maxV])

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)

    mask = cv.inRange(hsv, min, max)

    kernel = np.ones((3,3), np.uint8)
    ret, thresh = cv.threshold(mask, 127, 255, cv.THRESH_BINARY_INV)

    dilate = cv.dilate(thresh,(10,10), 3)
    opening = cv.morphologyEx(dilate, cv.MORPH_OPEN, kernel, iterations=2)

    bitwise = cv.bitwise_or(img, img, mask=opening)
    cv.imshow("bit9" , bitwise)

    gray = cv.cvtColor(bitwise, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(gray, 120,175,3)

    adaptive = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,3,2)

    dilate = cv.dilate(adaptive, (10, 10), 3)

    ret, thresh1 = cv.threshold(mask, 127, 255, cv.THRESH_BINARY_INV)

    thresh2 = cv.morphologyEx(thresh1, cv.MORPH_CLOSE, kernel, iterations=2)

    contours, hierarchies = cv.findContours(thresh2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv.contourArea(cnt)
        if area >= 50:
            cv.drawContours(img, [cnt],-1, (0,255,0), 2)

    # cv.imshow("cannys", canny)
    # cv.imshow("adaptive", thresh2 )
    # cv.imshow("testting", img)

    return contours