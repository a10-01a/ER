import cv2 as cv
class CameraControl:
    def __init__(self):
        self.cap = cv.VideoCapture(0)
    
    def getFrame(self):
        ret, frame = self.cap.read()
        return frame
    
    def stopCamera(self):
        self.cap.release()
        return 0
