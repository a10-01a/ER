import cv2 as cv
from datetime import date, datetime


class FaceDetect():
    def __init__(self, frame, xmlPath):
        self.frame = frame
        self.xmlPath = xmlPath

    def detectFaces(self, frame):
        self.frame = frame
        gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        cascade = cv.CascadeClassifier(self.xmlPath)
        self.faces = cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=20,
            minSize=(30, 30)
        )
        for (x, y, w, h) in self.faces:
            cv.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 10)
        return self.frame

    def getFaces(self, frame):
        self.cropFaces = []
        self.frame = frame
        gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        cascade = cv.CascadeClassifier(self.xmlPath)
        self.faces = cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=20,
            minSize=(30, 30)
        )
        for (x, y, w, h) in self.faces:
            self.cropFaces.append(self.frame[y:y+h, x:x+w])
        return self.cropFaces

    def showFaces(self, faces):
        i = 1
        for face in faces:
            cv.imshow(str(i), face)
            i += 1
        cv.waitKey()
        cv.destroyAllWindows()

    def saveFaces(self, faces, path):
        for face in faces:
            day = datetime.now().strftime("%b-%d")
            time = datetime.now().strftime("%H-%M-%f")
            cv.imwrite(f'{path}\{day}_{time}.png', face)

    def saveImage(self, image, path):
        day = datetime.now().strftime("%b-%d")
        time = datetime.now().strftime("%H-%M-%f")
        cv.imwrite(f'{path}\{day}_{time}.png', image)
