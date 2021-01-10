import PyQt5
import cv2 as cv
from faceDetect import *
from cameraControl import *

def main():
    camctrl = CameraControl()
    frame = camctrl.getFrame()
    camctrl.stopCamera()

    fd = FaceDetect(frame)
    faces = fd.getFaces(frame)
    cv.imshow("aaa", faces)
    cv.waitKey()

    


if __name__ == "__main__":
    main()
    