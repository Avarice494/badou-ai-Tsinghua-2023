import cv2
import numpy as np


def function(img, oh, ow):
    h, w, c = img.shape

    sh = oh / h
    sw = ow / w
    over = np.zeros((oh, ow, c), dtype=img.dtype)

    """
    1.i,j负责定位，与最邻近插值中的i，j效果一样，就是负责生成图相的像素点赋值
    2.本次循环的目的生成点，就是求出本次循环中的i,j与mode中的xy的对应关系
    3.y与y0 x与x0 就是见一的关系，如果在边缘取边缘即可
    4.先求出x，x向下取整就是x0，x0加1就是x1（忽略报错细节）
    5.根据给出的公式直接带入就行  
    """

    for i in range(oh):
        for j in range(ow):
            # x,y
            x = (i + 0.5) / sh - 0.5
            y = (j + 0.5) / sw - 0.5

            # x0
            x0 = int(np.floor(x))
            y0 = int(np.floor(y))
            # x1,y1
            x1 = min(x0 + 1, h - 1)
            y1 = min(y0 + 1, w - 1)

            tmp_x = (x1 - x) * img[x0, y0] + (x - x0) * img[x0, y1]
            tmp_y = (x1 - x) * img[x1, y0] + (x - x0) * img[x1, y1]

            over[i, j] = (y1 - y) * tmp_x + (y - y0) * tmp_y

    return over


if __name__ == '__main__':
    img = cv2.imread("lenna.png")

    over = function(img, 800, 800)

    cv2.imshow("hhaha", over)
    cv2.waitKey(0)
