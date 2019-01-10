from picamera import PiCamera
import RPi.GPIO as GPIO
import sys
import os
import shutil
import time
import datetime

myCamera = PiCamera()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

date = None

projectName = None
fileName = None
frame = 0
textCounter = 0
buttonDown = False

def padNum(num):
    num = str(num)
    if(len(num) == 1):
        return "00" + num
    elif(len(num) == 2):
        return "0" + num
    else:
        return num

try:    #main loop:

    #only accept project name if it doesn't already exist
    while projectName == None:
        projectName = input("Input Project Name: ").replace(" ", "_")
        fileName = "Stop_Motion/" + projectName
        try:
            os.mkdir(fileName)
            print("Created project " + projectName)
        except FileExistsError:
            if(input("Project already exists. Do you want to overwrite? y/n: ") == 'y'):
                shutil.rmtree(fileName)
                os.mkdir(fileName)
                print("Created project " + projectName)
            else:
                projectName = None
        except:
            print(sys.exc_info()[1])
            projectName = None
            
    myCamera.start_preview()
    while True:
        if(GPIO.input(17) > 0):
            if(buttonDown == False):
                #fileName = projectName + "_" + padNum(frame) + ".jpg"
                myCamera.capture("Stop_Motion/" + projectName + ("/%03d.jpg" % frame))
                print("Captured Frame %03d" % frame)
                frame += 1
                textCounter = 100
                buttonDown = True
        else:
            buttonDown = False

        if(textCounter > 0):
            textCounter -= 1
            myCamera.annotate_text = "Captured Frame %03d" % frame
        elif(textCounter == 0):
            myCamera.annotate_text = ""
            textCounter = -1
except:
    print(sys.exc_info()[1])
    myCamera.close()
finally:
    myCamera.close()
