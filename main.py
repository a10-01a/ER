import PyQt5
from cameraControl import CameraControl
from faceDetect import FaceDetect
import cv2 as cv

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
    