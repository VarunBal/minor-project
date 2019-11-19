import cv2 as cv
import glob
import os
import database as db

cap = cv.VideoCapture(0)
cascades = {}

while True:
    _,frame = cap.read()
    bw_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    for file in glob.glob('haarcascades\*.xml'):
        name = os.path.basename(file)[:-4]
        cascades[name] = cv.CascadeClassifier(file)

    for key in cascades:
        items = cascades[key].detectMultiScale(bw_frame)
        
        for (x,y,w,h) in items:
##            cv.rectangle(frame,(x,y),(x+w,y+h),255,2)
            font = cv.FONT_HERSHEY_SIMPLEX
            info = db.food_data(key)
            print(info)
            cv.putText(frame,str(key),(x,y),font,0.5,(0,255,255),2,cv.LINE_AA)
            break

    cv.imshow('detected',frame)

    if cv.waitKey(1) & 0xff == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
