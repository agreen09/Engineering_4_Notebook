Pi in the Sky
======
This is the project page for Barrett and Amara's Pi in the Sky project.
The media and files for this project are located [here](https://drive.google.com/drive/folders/1esaPi3y6qm1p5ZarPjROJN2QxnBNeMxv?usp=sharing).

Planning
------

Project Goal
------
The goal for this project is to get a Raspberry Pi into the air by any means necessary, collecting data along the way.

We will be using a model rocket to launch our Raspberry Pi ~1000ft into the air.

Materials
------
To create our project, we will be using:
*A 3d printer + plastic
*A laser cutter + 3.75mm acrylic
*An Estes model rocket kit
*A Raspberry Pi Zero
*A PowerBoost 500C (to power the Pi)
*A 3.7v battery
*An Adafruit LSM303DLHC accelerometer
*A soldering iron

Initial Design
------
Luckily enough, the Sigma Lab already has some model rocket kits so we will not have to purchase any. 

We will be designing an apparatus to attach all components to the rocket. It will fit around its body snugly so that it cannot slide off. All components, including the Raspberry Pi, battery chip, lithium battery, and accelerometer should fit onto this apparatus.

Potential Roadblocks
------
We may run into a few problems during the course of our project that we will need to solve. These include:
*Model rockets are very precise and the addition of extra components may prevent it from taking off properly
*Since we can't drill any holes into the rocket itself, we will have to design an apparatus to attach the Pi to the rocket

Planned Schedule
------
We will try to complete each phase of our project by the following deadlines:

| Goal | Part of project | Actual completion
--- | --- | --- 
October 26, 2018 | We will have completed all planning for our project. We will have a clear idea of how each component will work and we will be able to begin designing. |
November 2, 2018 | All components that will be 3d printed will be fully designed in SolidWorks so we can print and test. A rough draft of our code will be written as well. |
November 16, 2018 | We anticipate that revisions to our design will be necessary, so we will have the final draft of all components designed in SolidWorks. |
November 30, 2018 | We are giving ourselves two weeks of testing to ensure that our design is complete. It is too early to anticipate how well our design will work, but we hope to complete our project by this date. |
December 7, 2018 | By this point, our project will be complete and all documentation will be written. If our project is not complete for any reason, we will begin wrapping it up. |

Code
------
````python
from subprocess import call
from time import sleep
import time
import socket
import os
import sys
import time
import datetime
import Adafruit_LSM303
import Adafruit_BMP.BMP085 as BMP085
import RPi.GPIO as GPIO
import gspread
import math
from oauth2client.service_account import ServiceAccountCredentials
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
 
sensor = BMP085.BMP085()
lsm303 = Adafruit_LSM303.LSM303()
 
ipaddr = "---.---.---.---"
online = False
 
worksheet = None
string = None
freq = 1
 
fileName =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dataFile = "Data/" + fileName
f = open(dataFile, "w+")
f.close()
data = []
pointer = 0
 
errorFile = "log.txt"
#f = open(fileName, "w")
#f.close()
 
EMAIL = ['bcrusse13@charlottesvilleschools.org',
         'agreen09@charlottesvilleschools.org']
NAME = str("[PI_DATA] " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
 
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
 
def login_open_sheet(email, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    	#gc = gspread.login(email, password)
    credentials = ServiceAccountCredentials.from_json_keyfile_name('pi-in-the-sky-13-ca776cc8e6db.json', scope)
    gc = gspread.authorize(credentials)
    sh = gc.create(spreadsheet)
    for i in range(0, len(EMAIL)):
        sh.share(EMAIL[i], perm_type='user', role='writer', notify=False)
 
    print ('Logged in successfully. New worksheet created\n')
    return sh.sheet1
 
def isOnline():
    gw = os.popen("ip -4 route show default").read().split()
    if(len(gw) > 0):
        return True
    else:
        return False
 
def getLine(index, incPointer=True):
    global pointer
    f = open(dataFile, "r")
    d = f.readlines()
    f.close()
    if(index == -1):
        return d
    else:
        pointer += 1
        return d[index]
 
def fileLen():
    f = open(dataFile, "r")
    d = f.readlines()
    f.close()
    return len(d)
 
def fileWrite(string):
    f = open(dataFile, "a")
    f.write(string)
    f.close()
    return 1
 
 
start = time.time()
loopStart = None
timeCheck = None
 
def elapsed():
    return time.time() - start
 
def getTime():
    return datetime.datetime.now().strftime("%H:%M:%S")
 
def main():
    global worksheet
 
    elapsed()
 
    if worksheet is None:
        print ('Logging in...')
        worksheet = login_open_sheet(EMAIL, NAME)
        worksheet.append_row(('Time', 'Temp', 'Pressure', 'Altitude', 'Accel X', 'Accel Y', 'Accel Z', 'Mag X', 'Mag Y', 'Mag Z'))
 
    temp = sensor.read_temperature()
    pressure = sensor.read_pressure()
    altitude = sensor.read_altitude()
 
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
 
 
    tempStr = str(temp)
    pressureStr = str(pressure)
    altitudeStr = str(altitude)
 
    print ('Temperature: ' + str(temp) + ' C')
    print ('Pressure: ' + str(pressure) + ' Pa')
    print ('Altitude: ' + str(altitude) + ' m')
 
    #try:
    #json.dumps(my_dictionary, indent=4, sort_keys=True, default=str)
 
    fileWrite(getTime() + ", " + tempStr + ", " + pressureStr + ", " + altitudeStr + ",  [" + str(accel_x) + ", " + str(accel_y) + ", " + str(accel_z) + "], [" + str(mag_x) + ", " + str(mag_y) + ", " + str(mag_z) + "]\n")
    if(isOnline()):
        #timeCheck = elapsed()
        #while(pointer < len(getLine(-1)) and elapsed() - timeCheck < freq - 0.5 and isOnline()): 
            #data = getLine(pointer).split(", ")
            #worksheet.append_row((str(data[0]), str(data[1]), str(data[2]), str(data[3])))
            worksheet.append_row((getTime(), tempStr, pressureStr, altitudeStr, str(accel_x), str(accel_y), str(accel_z), str(mag_x), str(mag_y), str(mag_z)))
            #print ('Wrote a row to ' + NAME + '\n')
            #print(str(data[1]), ", ", str(data[2]), ", ", str(data[3]))
 
    #except:
        # Error appending data, most likely because credentials are stale.
        # Null out the worksheet so a login is performed at the top of the loop.
        #print ('Append error, logging in again')
        #worksheet = None
        #time.sleep(freq)
        #continue
 
while True:
    try:
        loopStart = elapsed()
        main()
        while(elapsed() - loopStart < freq):
            sleep(0.01)
        print("\n___\n")
    except Exception as e:
        f = open(errorFile, "a+")
        f.write(str(fileName) + "\n")
        f.write(str(e) + "\n\n")
        f.close()
        print(e)
        exit()
````

Work Log
------
Milestone? | Date | Summary
--- | --- | --- 
Initial Pi holder design completed | Mid-October? | Finished the initial design of the part which attaches all of our chips to the rocket
Lightened Pi holder completed | 11/15/18 | Finished lightening the Pi holder, separating it into two parts, and started printing
Chip models made | 11/19/18 | Finished and uploaded Solidworks versions of Powerboost and accelerometer, which the library didn't have models of
Battery sleeve started | 11/26/18 | Made a small part to test dimensions of a sleeve to hold the battery. The original part didn't have anything to hold the batter in place, and making a separate part to test meant we could get it right without wasting material of a full pi holder
Battery sleeve printed | 11/29/18 | Printed the finalized prototype battery sleeve and incorporated the design into the Pi holder
Code written | 12/13/18 | Finished code
Rocket assembled | 12/13/18 | Fully assembled model rocket 
Wired everything | January | Added all sensors and chips to the rocket, fixed the ones that didn't work
Pi Holder 2 finished | January | Printed bigger holder and got it wired
First launch | Soon? | First launch of the rocket
