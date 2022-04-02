import sys
sys.path.insert(0, "./Navigation_Center")
import numpy as np
import cv2 as cv
from resize_img import resize as rs
from Navigation_Center.navigation_center import Navigation

# import img here
img = cv.imread("./Test_Data/lua.jpg")
img = rs(img)


def main(img):

    while True:

        # use package here
        gn = Navigation(img)
        gn.detect_damege_seeds()

        cv.imshow("nothing", img)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    cv.destroyAllWindows()


# start from here
if __name__ == "__main__":
    main(img)