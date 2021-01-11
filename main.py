import PyQt5
import cv2 as cv
from faceDetect import *
from cameraControl import *

def main():
    # camctrl = CameraControl()
    # frame = camctrl.getFrame()
    # camctrl.stopCamera()
    frame=cv.imread('./10people.jpg')
    fd = FaceDetect(frame, './face.xml')
    faces = fd.getFaces(frame)
    fd.showFaces(faces)

    


if __name__ == "__main__":
    main()
    