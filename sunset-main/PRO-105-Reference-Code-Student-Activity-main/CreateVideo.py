import cv2
import os
path = 'sunset-main/PRO-105-Reference-Code-Student-Activity-main/Images'
imgs = []
allimg = os.listdir(path)
for a in allimg:
    filename = path + '/' + a
    imgs.append(filename)
firstimg = cv2.imread(imgs[0])
height,width,channels = firstimg.shape
size = (width,height)
newvideo = cv2.VideoWriter('sunset.mp4',cv2.VideoWriter_fourcc(*'DIVX'),120,size)
for i in imgs:
    frame = cv2.imread(i)
    newvideo.write(frame)
newvideo.release()
cv2.destroyAllWindows()