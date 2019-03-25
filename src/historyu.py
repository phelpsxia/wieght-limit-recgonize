import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
pic = cv2.imread('nums.jpg',0)
ret,thresh1 = cv2.threshold(pic,127,255,cv2.THRESH_BINARY_INV)
def s(X):
    cv2.imshow('',X)
    cv2.waitKey(0)
s(pic)
s(thresh1)
sum0 = np.sum(thresh1,0)

im = thresh1
area = []
pos = []
for i in range(im.shape[1]):
    area.append(sum0[i]/im.shape[0])
    s = 0
    for j in range(im.shape[0]):
        s += im[j,i]*j**2
    s = s/im.shape[0]
    pos.append(s)

x = np.arange(0,im.shape[1],1)
myticks = np.arange(0,800,20)
   
plt.figure(2)
plt.subplot(211)
plt.xticks(myticks)
plt.scatter(x,np.asarray(area), alpha=0.6)

plt.subplot(212)
plt.scatter(x,pos, alpha=0.6)
plt.xticks(myticks) 
plt.show()

# cut =122

from digit_seg import find_several_min_points

c = find_several_min_points(area, 30,55)
print(c)

ls = []#shupai
us = []#hengpai 
lp = []#jiaquan
up = []

ls = [area[:60], area[80:138], area[160:215], area[240:293], area[320:370], area[393:445], area[468:520], area[560:600], area[623:680],area[703:757]]
us = [pos[:60], pos[80:138], pos[160:215], pos[240:293], pos[320:370], pos[393:445], pos[468:520], pos[560:600], pos[623:680],pos[703:757]]

ims=   [im[:,:60], im[:,80:138], im[:,160:215], im[:,240:293], im[:,320:370], im[:,393:445], im[:,468:520], im[:,560:600], im[:,623:680],im[:,703:757]]

pkl.dump(ls, open("ls.pkl", "wb"))

pkl.dump(us, open("us.pkl", "wb"))

pkl.dump(ims, open("ims.pkl","wb"))

"""
d1 = np.fft.fft(s1, 1000) #不能取100，小于奈奎斯特频率
d2 = np.fft.fft(s2, 1000)
d3 = np.fft.fft(s3, 1000)
print(d1.shape)
plt.figure(1)

plt.subplot(311)
plt.plot(d1)
plt.grid(True)

plt.subplot(312)
plt.plot(d2)
plt.grid(True)


plt.subplot(313)
plt.plot(d3)
plt.grid(True)
plt.show()
"""


