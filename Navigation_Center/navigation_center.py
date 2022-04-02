

import os
import sys
import numpy as np
import cv2 as cv

from Detect_file_packages.damage_seeds_detect  import damege_seeds_detect as dsd
from Detect_file_packages.trees_shape_detect import trees_shape_detect as tsd
from Detect_file_packages.white_background_detect import white_background_detect as wbd

def Navigation(img):

    dsd(img)




