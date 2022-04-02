
import os
import sys
import cv2 as cv
import numpy as np

def nothing(x):
    pass

# cv.namedWindow("remove_white")
#
# cv.createTrackbar("min-H", "remove_white", 0, 255, nothing)
# cv.createTrackbar("min-S", "remove_white", 45, 255, nothing)
# cv.createTrackbar("min-V", "remove_white", 0, 255, nothing)
#
# cv.createTrackbar("max-H", "remove_white", 40, 255, nothing)
# cv.createTrackbar("max-S", "remove_white", 255, 255, nothing)
# cv.createTrackbar("max-V", "remove_white", 255, 255, nothing)


def white_background_detect(img):

    # minH = cv.getTrackbarPos("min-H", "remove_white")
    # minS = cv.getTrackbarPos("min-S", "remove_white")
    # minV = cv.getTrackbarPos("min-V", "remove_white")
    # maxH = cv.getTrackbarPos("max-H", "remove_white")
    # maxS = cv.getTrackbarPos("max-S", "remove_white")
    # maxV = cv.getTrackbarPos("max-V", "remove_white")
    #
    # min = np.array([minH, minS, minV])
    # max = np.array([maxH, maxS, maxV])


    min = np.array([0, 45, 0])
    max = np.array([40, 255, 255])

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, min, max)
    canny = cv.Canny(mask, 60, 165, 3)
    dilate = cv.dilate(canny, (10, 10), iterations=2)

    ret, thresh = cv.threshold(mask, 127, 255, cv.THRESH_BINARY_INV)

    bitwise = cv.bitwise_and(img, img, mask=thresh)
    # remove white out img
    # cv.imshow("white remove", bitwise)

    contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    final = cv.drawContours(img.copy(), contours, -1, (0, 0, 255), 1)

    return final, contours
