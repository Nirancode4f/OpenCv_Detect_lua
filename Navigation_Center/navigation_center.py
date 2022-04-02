
import cv2 as cv
from Detect_file_packages.damage_seeds_detect  import damege_seeds_detect as dsd
from Detect_file_packages.trees_shape_detect import trees_shape_detect as tsd
from Detect_file_packages.white_background_detect import white_background_detect as wbd

class Navigation:
    def __init__(self, img):
        self.img = img

    def detect_damege_seeds(self):
        # detect dameged seed
        dame_seeds, contours = dsd(self.img)
        cv.imshow(" damge seed", dame_seeds)

    def detect_white(self):
        # detect white
        white_detect, white_contours = wbd(self.img)
        cv.imshow("white detected", white_detect)

    def detect_trees(self):
        # trees trees
        trees_detect, trees_contours = tsd(img)
        cv.imshow("trees detected", trees_detect)








# def Navigation(img):








