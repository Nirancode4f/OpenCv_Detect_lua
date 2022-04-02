import sys
sys.path.insert(0, "./Navigation_Center")
sys.path.insert(0, "./Detect_file_packages")
import numpy as np
import cv2 as cv
from resize_img import resize as rs
from navigation_center import test


# import img here
img = cv.imread("./Test_Data/lua.jpg")
img = rs(img)



def main(img):

    while True:

        # remove_white

        test()

        # remove_trees

        # Detect_dameged_seeds


        cv.imshow("nothing", img)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    cv.destroyAllWindows()


# start from here
if __name__ == "__main__":
    main(img)