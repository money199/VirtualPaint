import cv2
import numpy as np
frameWidth =640
frameHeight =400
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,130)  #mode,brightness
# list of values of colors (violet,black ,green)
# [h_min,s_min,v_min,h_max,s_max,v_max]
myColors=[[0,0,231,180,18,255]]
myPoints=[] #x,y

def getContours(img):
    # cv2.RETR_EXTERNAL get the extrme cornes(mode)
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # -1 : all the index
        print(area)
        # cancellation of NOise

        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (0, 0, 0), 3)
            # calculate curve length  (helps in detection of cornors of out image)/perimeter
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)  # (contour,random resolution ,shape is  closed or not)
            x, y, w, h = cv2.boundingRect(approx)  # bounding block dimensions over shape (whose coordinates are approx)
    return  x+w//2,y

def findColor(img,myColors):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    newPoint=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y =getContours(mask)
        cv2.circle(imgResult,(x,y),10,(255,255,255),cv2.FILLED)
        #cv2.imshow(str(i),mask)
        if x!=0 and y!=0:
            newPoint.append([x,y])
    return newPoint

def drawOnCanvas(myPoints):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,(255,255,255),cv2.FILLED)

while True:
    sucess,img =cap.read()

    imgResult=img.copy()

    newPoints=findColor(img,myColors)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints)
    cv2.imshow("image", imgResult)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
cv2.destroyAllWindows()