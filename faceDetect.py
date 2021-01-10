import cv2 as cv

class FaceDetect():
    def __init__(self, frame):
        self.frame = frame
        self.xmlPath = './face.xml'

    def getFaces(self, frame):
        self.frame = frame
        gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        cascade = cv.CascadeClassifier(self.xmlPath)
        self.faces = cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        for (x, y, w, h) in self.faces:
            cv.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return self.frame

    def showFaces(self):
        cv.imshow('Img', self.faces)
        cv.waitKey()
