import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def nothing(x):
    pass


img = cv.imread("./TEST_DATA/lua4.jpg")
img = cv.resize(img, (800, 800))

cv.namedWindow("mainframe")

cv.createTrackbar("min-H", "mainframe", 0, 255, nothing)
cv.createTrackbar("min-S", "mainframe", 116, 255, nothing)
cv.createTrackbar("min-V", "mainframe", 0, 255, nothing)

cv.createTrackbar("max-H", "mainframe", 22, 255, nothing)
cv.createTrackbar("max-S", "mainframe", 255, 255, nothing)
cv.createTrackbar("max-V", "mainframe", 255, 255, nothing)

while (1):

    minH = cv.getTrackbarPos("min-H", "mainframe")
    minS = cv.getTrackbarPos("min-S", "mainframe")
    minV = cv.getTrackbarPos("min-V", "mainframe")
    maxH = cv.getTrackbarPos("max-H", "mainframe")
    maxS = cv.getTrackbarPos("max-S", "mainframe")
    maxV = cv.getTrackbarPos("max-V", "mainframe")

    min = np.array([minH, minS, minV])
    max = np.array([maxH, maxS, maxV])

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, min, max)
    canny = cv.Canny(mask, 60, 165, 3)

    # cv.imshow("main.py", img)
    cv.imshow("default", img)
    cv.imshow("main", hsv)
    cv.imshow("canny", canny)

    dilate = cv.dilate(canny, (10, 10), iterations=1)
    cv.imshow("dilate", dilate)

    contours, hierarchies = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    final = cv.drawContours(img.copy(), contours, -1, (255, 0, 0), 2)
    cv.imshow("final", final)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.destroyAllWindows()
