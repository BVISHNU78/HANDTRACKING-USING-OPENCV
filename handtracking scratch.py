import cv2
import mediapipe as mp
import time
class handDetector():
    def __init__(self,mode=False,maxHands=2,modelC=1,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.modelC=modelC
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mpHands =mp.solutions.hands
        self.hands =self.mpHands.Hands(self.mode,self.maxHands,self.modelC,self.detectionCon,self.trackCon)
        self.mpDraw =mp.solutions.drawing_utils
    def findHands(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results= self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self,img,handNo=0,draw=True):
        lmlist=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                height,width,channel=img.shape
                cx,cy=int(lm.x*width),int(lm.y*height)
                print([cx,cy])
                #lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),3,(255,0,255),cv2.FILLED)
        return lmlist        
    
def main():
    PRTime=0
    CURTime=0
    cap=cv2.VideoCapture(0)
    detector=handDetector() 
    while True:
        success,img = cap.read()
        img=detector.findHands(img)
        lmList=detector.findPosition(img)
        if len(lmList)!= 0:
            print(lmList[4])
        CURTime=time.time()
        fps=1/(CURTime-PRTime)
        PRTime=CURTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("image",img)
        cv2.waitKey(1) 
if __name__=="__main__":
    main()
