import cv2
import numpy as np


def function(img, oh, ow):
    h, w, c = img.shape
    sh = oh / h
    sw = ow / w
    over = np.zeros((oh, ow, c), dtype=img.dtype)
    for i in range(oh):
        for j in range(ow):
            x = int(i / sh)
            y = int(j / sw)
            over[i, j] = img[x, y]
    return over


if __name__ == '__main__':
    img = cv2.imread("lenna.png")
    over = function(img, 2000, 2000)

    cv2.imshow("test", over)
    cv2.waitKey(0)
