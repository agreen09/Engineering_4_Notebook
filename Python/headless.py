from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303
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

lsm303 = Adafruit_LSM303.LSM303()

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

data = []
length = 25
graphWidth = 110
graphHeight = 50
xPadding = width - graphWidth
spacing = graphWidth / length
yAxisText = 'a(m/s^2)'
batteryFull = None
showIcon = False
flashCounter = 0

def mapNum(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

while True:
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag

    accel_x /= 100
    accel_y /= 100
    accel_z /= 100
    
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    data.append(accel_x)
    if(len(data) > length) :
        data.pop(0)

    draw.line((xPadding, 5, xPadding, graphHeight), fill=255)
    draw.line((xPadding, graphHeight, width - 5, graphHeight), fill=255)
    draw.text((width / 2, graphHeight + 5), 't(s)', font=font, fill=255)

    rotImg = Image.new('1',
                    (font.getsize(yAxisText)[0] + 2,
                     font.getsize(yAxisText)[1] + 2), color=0)
    rotDraw = ImageDraw.Draw(rotImg)
    rotDraw.text((0, 0), yAxisText, fill=255)
    rotImg = rotImg.rotate(90, expand=1)
    image.paste(rotImg, (2, top))
    
    for x, y in enumerate(data):
        if(x < len(data) - 1):
            draw.line((
                (x * spacing) + xPadding,
                ((mapNum(y, -10, 10, 0, graphHeight))),
                ((x + 1) * spacing) + xPadding,
                ((mapNum(data[x + 1], -10, 10, 0, graphHeight)))),
                fill=255)

    batteryFull = GPIO.input(17)

    if(flashCounter > 1):
        showIcon = False if(showIcon) else True
        flashCounter = 0
    else:
        flashCounter += 1

    if(showIcon and batteryFull == 0):
        draw.rectangle((width - 20, 4, width - 7, 10), outline=255, fill=0)
        draw.rectangle((width - 20, 4, width - 17, 10), outline=255, fill=255)
        draw.rectangle((width - 7, 6, width - 5, 8), outline=255, fill=255)
    elif(batteryFull == 1):
        draw.rectangle((width - 20, 4, width - 7, 10), outline=255, fill=0)
        draw.rectangle((width - 20, 4, width - 11, 10), outline=255, fill=255)
        draw.rectangle((width - 7, 6, width - 5, 8), outline=255, fill=255)
    disp.image(image)
    disp.display()
    sleep(0.01)

    
    
