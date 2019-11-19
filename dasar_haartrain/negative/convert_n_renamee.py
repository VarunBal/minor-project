import cv2 as cv
import glob
import os

count = 1

for file in glob.glob('*.jpg'):
    name = os.path.basename(file)[:-4]

    img = cv.imread(file)
    resized_img = cv.resize(img, (640, 480))
    cv.imwrite(file,resized_img)
    print(count,'done')
    count+=1

