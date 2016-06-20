# -*- encoding: utf-8 -*-
# Author: Epix
import cv2
import sys


def make_mosainic(input_files, output_file):
    if sys.platform == 'win32':
        result = (0, cv2.imread('cache/r.jpg'))
    else:
        stitcher = cv2.createStitcher(False)
        result = stitcher.stitch(tuple(cv2.imread(fn) for fn in input_files))
    cv2.imwrite(output_file, result[1])
    return result[1].shape[:2]


if __name__ == '__main__':
    make_mosainic(['bryce_left_02.png', 'bryce_right_02.png'], 'result.jpg')
