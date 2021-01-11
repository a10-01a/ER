import cv2 as cv

class FaceDetect():
    def __init__(self, frame, xmlPath):
        self.frame = frame
        self.xmlPath = xmlPath

    def getFaces(self, frame):
        self.cropFaces = []
        self.frame = frame
        gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        cascade = cv.CascadeClassifier(self.xmlPath)
        self.faces = cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=25,
            minSize=(30, 30)
        )
        for (x, y, w, h) in self.faces:
            self.cropFaces.append(self.frame[y:y+h,x:x+w])
            cv.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return self.cropFaces

    def showFaces(self, faces):
        i = 0
        for face in faces:
            cv.imshow(str(i), face)
            i+=1
        cv.waitKey()
        cv.destroyAllWindows()
