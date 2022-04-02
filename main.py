import sys
sys.path.insert(0, "./Navigation_Center")
import numpy as np
import cv2 as cv
from resize_img import resize as rs
from Navigation_Center.navigation_center import Navigation

# import img here
img = cv.imread("./Test_Data/lua.jpg")

def main(img):

    while True:

        ##### use package here (import class navigation) #####
        gn = Navigation(rs(img))  #  👈(ﾟヮﾟ👈) code mệt lắm đấy.

        ##### call object im package #####
        gn.detect_damege_seeds()
        gn.detect_trees()
        gn.detect_white()


        cv.imshow("nothing", rs(img))
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    cv.destroyAllWindows()




# start from here
if __name__ == "__main__":
    main(img)

#