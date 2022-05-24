


import cv2 as cv
import numpy as np


capture = cv.VideoCapture(0)


def nothing(x):
    pass
cv.namedWindow("Settings")
cv.namedWindow("Canny")
cv.createTrackbar("min-H","Settings", 0, 255, nothing)
cv.createTrackbar("min-S","Settings", 189, 255, nothing)
cv.createTrackbar("min-V","Settings", 135, 255, nothing)
cv.createTrackbar("max-H","Settings", 255, 255, nothing)
cv.createTrackbar("max-S","Settings", 255, 255, nothing)
cv.createTrackbar("max-V","Settings", 255, 255, nothing)

cv.createTrackbar("min-canny", "Canny", 100, 200, nothing)
cv.createTrackbar("max-canny", "Canny", 200, 200, nothing)


        # if cv.VideoCapture(0) -> Using webcam in laptop to collect video
while True:
    isTrue, frame = capture.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    minH = cv.getTrackbarPos("min-H", "Settings")
    minS = cv.getTrackbarPos("min-S", "Settings")
    minV = cv.getTrackbarPos("min-V", "Settings")
    maxH = cv.getTrackbarPos("max-H", "Settings")
    maxS = cv.getTrackbarPos("max-S", "Settings")
    maxV = cv.getTrackbarPos("max-V", "Settings")

    minCanny = cv.getTrackbarPos("min-canny", "Canny")
    maxCanny = cv.getTrackbarPos("max-canny", "Canny")

    lowerb = np.array([minH,minS,minV])
    upperb = np.array([maxH,maxS,maxV])
    
    kernel = np.ones((5,5), np.uint8)

    Mask = cv.inRange(hsv, lowerb, upperb)
    
    canny = cv.Canny(Mask, minCanny, maxCanny, 8  )

    sure_bg = cv.dilate(canny, kernel, iterations=5)
    opening = cv.morphologyEx(sure_bg,cv.MORPH_OPEN,kernel, iterations = 5)



    cv.imshow("hsv", hsv)
    cv.imshow("Mask", Mask)
    cv.imshow("canny" , canny)
    cv.imshow("opening", opening)
    cv.imshow('sure_bg', sure_bg);

    print(f' lowerb =  {lowerb} \n upperb = {upperb}')

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# img = cv.imread("./TEST_DATA/lua.jpg")
#
# size = round((img.shape[0]/4) ), round((img.shape[1]/2))
#
# print(size)
#
# img = cv.resize(img, (size))
#
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#
# cv.imshow("main.py", img)
# cv.imshow("hsv",hsv)
#
# cv.waitKey(0)