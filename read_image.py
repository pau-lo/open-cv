import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np


def read_image():
    # Read image
    root = os.getcwd()
    # print("root:", root)
    img_path = os.path.join(root, "./open-cv/sample-images/baby-color-kitten.jpg")
    img = cv.imread(img_path)
    # debug - in order to view the matrix of the image
    # debug = 1
    # Display image
    cv.imshow("img", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    read_image()
