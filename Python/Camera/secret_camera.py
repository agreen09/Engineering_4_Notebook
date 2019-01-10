from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

date = None
isRecording = False

myCamera = PiCamera()

while True:
    if(GPIO.input(17) > 0 and isRecording == False):
        date = datetime.datetime.now().strftime("%d-%m-%y_%H:%M:%S")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        fileName = "secret_recording~" + date
        myCamera.start_recording("/Secret_Camera/" + fileName + ".h264")
        print("STARTED RECORDING: " + time)
        isRecording = True
