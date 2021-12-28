import cv2
import mediapipe as mp
import HandTrackingModule as htm
import time
PRTime=0
CURTime=0
cap=cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.5, maxHands=2)
while True:
    success,img = cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    if len(lmList)!= 0:
        print(lmList[4])
        CURTime=time.time()
        fps=1/(CURTime-PRTime)
        PRTime=CURTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("image",img)
        cv2.waitKey(1) 