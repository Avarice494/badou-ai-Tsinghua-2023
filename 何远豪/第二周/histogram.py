import cv2
import matplotlib.pyplot as plt


img = cv2.imread("lenna.png",flags=1)


plt.subplot(221)
plt.imshow(img)

plt.subplot(222)
plt.hist(img.ravel(), 256)


hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(223)
plt.title("Grayscale Histogram")
plt.xlabel("Bins")#X轴标签
plt.ylabel("# of Pixels")#Y轴标签
plt.plot(hist)
plt.xlim([0,256])#设置x坐标轴范围
plt.show()




image = cv2.imread("lenna.png")
cv2.imshow("Original",image)
#cv2.waitKey(0)

chans = cv2.split(image)
colors = ("b","g","r")
plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan,color) in zip(chans,colors):
    hist = cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist,color = color)
    plt.xlim([0,256])
plt.show()