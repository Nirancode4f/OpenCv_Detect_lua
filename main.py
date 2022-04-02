
import numpy as np
import cv2 as cv
from resize_img import resize as rs


# import img here
img = "./Test_Data/lua.jpg"
img = cv.imread(img)

# run this
def main(img):
    # asdfasdadsfasd

    img = rs(img)

    cv.imshow("nothing", img)

    cv.waitKey(0)




if _name_ == "_name_":
    main(img)