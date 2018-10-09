import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

inputVal = False

while True:
    inputVal = GPIO.input(17)

    if(inputVal > 0):
        GPIO.output(18, GPIO.HIGH)
        canTrigger = False
        counter = 20
        print("HIGH")
    else:
        GPIO.output(18, GPIO.LOW)
        print("LOW")
    sleep(0.25)
