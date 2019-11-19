import cv2 as cv
import glob

pic_num = 0

for file in glob.glob('rawdata\*.jpg'):
        print(file)
        img = cv.imread(file)
        img = cv.resize(img, (392, 695))
        cv.imwrite('rawdata\\' + str(pic_num) + '.bmp',img)
        pic_num += 1
