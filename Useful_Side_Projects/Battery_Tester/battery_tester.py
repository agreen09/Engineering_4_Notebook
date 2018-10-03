from subprocess import call
from time import sleep
import time
import datetime
import Adafruit_SSD1306
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
padding = 2
shape_width = 20
top = padding
bottom = height-padding
font = ImageFont.load_default()

fileName = str("batteryData.txt" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
f = open(fileName, "w")
f.close()

date = None
battery = None
string = None

while True:
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    battery = "HIGH" if(GPIO.input(17)) else "LOW"
    
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    string = str(date + ": " + str(battery) + "\n")
    print(string)

    f = open(fileName, "a")
    f.write(string)
    f.close()

    draw.text((5, 25), string, font=font, fill=255)

    disp.image(image)
    disp.display()
    
    sleep(10)
