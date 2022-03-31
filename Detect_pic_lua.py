

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from remove_white import remove_white as rmovew
img = cv.imread("./TEST_DATA/lua2.jpg")

img = cv.resize(img, (1000,1000) )


def remove_tree(min,max):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, min, max)

    canny = cv.Canny(mask, 60, 165, 3)
    # damaged seeds detect
    dilate = cv.dilate(canny, (10, 10), iterations=2)
    ret, thresh = cv.threshold(mask, 127, 255, cv.THRESH_BINARY_INV)

    # import mask to img . (remove tree)

    contours, hierarchies = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    # white remove
    bitwise = cv.bitwise_or(img, img, mask=thresh)
    cv.imshow("tesssting", bitwise)
    white_removed = rmovew(bitwise)

    return white_removed



def detect_rice(img):

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # ret , thresh = cv.threshold(gray, 127,255,   cv.THRESH_BINARY)

    threshhold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)

    kernel = np.ones((2, 2), np.uint8)

    opening = cv.morphologyEx(threshhold, cv.MORPH_OPEN, kernel)

    canny = cv.Canny(opening, 100, 168, 20)

    sure_bg = cv.dilate(canny, kernel, iterations=5)

    # opening = cv.morphologyEx(sure_bg, cv.MORPH_OPEN, kernel, iterations=5)









def nothing(x):
    pass






cv.namedWindow("remove_tree")

cv.createTrackbar("min-H", "remove_tree", 0, 255, nothing)
cv.createTrackbar("min-S", "remove_tree", 23, 255, nothing)
cv.createTrackbar("min-V", "remove_tree", 109, 255, nothing)

cv.createTrackbar("max-H", "remove_tree", 35, 255, nothing)
cv.createTrackbar("max-S", "remove_tree", 196, 255, nothing)
cv.createTrackbar("max-V", "remove_tree", 255, 255, nothing)



while (1):




    rminH = cv.getTrackbarPos("min-H", "remove_tree")
    rminS = cv.getTrackbarPos("min-S", "remove_tree")
    rminV = cv.getTrackbarPos("min-V", "remove_tree")
    rmaxH = cv.getTrackbarPos("max-H", "remove_tree")
    rmaxS = cv.getTrackbarPos("max-S", "remove_tree")
    rmaxV = cv.getTrackbarPos("max-V", "remove_tree")

    # seed
    min = np.array([0,94,0])
    max = np.array([21,255,255])
    #tree

    tree_min = np.array([rminH,rminS,rminV])
    tree_max = np.array([rmaxH,rmaxS,rmaxV])


    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, tree_min,tree_max)

    cv.imshow("masktestting", mask)


    canny = cv.Canny(mask, 60,165,3)
    # damaged seeds detect
    dilate = cv.dilate(canny , (10,10) , iterations=2)
    ret , thresh = cv.threshold(mask, 127,255,   cv.THRESH_BINARY_INV)

    # import mask to img . (remove tree)

    contours, hierarchies = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    #

    # white remove
    bitwise = cv.bitwise_or(img, img , mask=thresh)


    tree_remove_done = remove_tree(tree_min,tree_max)

    white_removed = rmovew(bitwise)



    final1 = cv.drawContours(img.copy(), contours, -1, (0, 0, 255), 1)
    cv.imshow("final1", final1)
    final2 = cv.drawContours(final1.copy(), white_removed, -1, (0, 255, 0),1)
    cv.imshow("final", final2)
    final3 = cv.drawContours(final2.copy(), white_removed, -1, (255, 0, 0), 1)
    cv.imshow("final3", final3)



    # detect rice
    # detect_rice(img)





    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.destroyAllWindows()






