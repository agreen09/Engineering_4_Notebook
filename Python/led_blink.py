import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

for i in range(1, 10):
    GPIO.output(17, GPIO.HIGH)
    sleep(1)
    GPIO.output(17, GPIO.LOW)
    sleep(1)
