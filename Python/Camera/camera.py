from picamera import PiCamera
from time import sleep

myCamera = PiCamera()
myCamera.start_preview()
sleep(5)
myCamera.close()
