from picamera import PiCamera
import sys
import time
import datetime

date = None
myCamera = PiCamera()
myCamera.start_preview()

try:
    for effect in myCamera.IMAGE_EFFECTS:
        date = datetime.datetime.now().strftime("%d-%m-%y_%H:%M:%S")
        myCamera.image_effect = effect
        myCamera.annotate_text = effect
        cmd = input()
        if(cmd == 's'):
            fileName = "image_capture_" + effect + "_" + str(date)
            myCamera.capture("/Camera_Effects/" + fileName + ".jpg")
except:
    print(sys.exc_info()[0])
    myCamera.close()
finally:
    myCamera.close()
