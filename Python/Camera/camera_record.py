from picamera import PiCamera
import sys
import time
import datetime

date = None

myCamera = PiCamera()
myCamera.start_preview()

try:
    while True:
        cmd = input()
        
        date = datetime.datetime.now().strftime("%d-%m-%y~~%H:%M:%S")
        if(cmd != ''):
            myCamera.annotate_text = "recording"
            fileName = "recording_" + date
            myCamera.start_recording("/Camera_Record/" + fileName + ".h264")
except:
    print(sys.exc_info()[0])
    myCamera.close()
finally:
    myCamera.close()
