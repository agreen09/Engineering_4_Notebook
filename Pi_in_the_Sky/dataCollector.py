from subprocess import call
from time import sleep
import time
import socket
import os
import sys
import time
import datetime
import Adafruit_BMP.BMP085 as BMP085
import RPi.GPIO as GPIO
import gspread
import math
from oauth2client.service_account import ServiceAccountCredentials

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

sensor = BMP085.BMP085()

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

EMAIL = 'bcrusse13@charlottesvilleschools.org'
NAME = str("[PI_DATA] " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

def login_open_sheet(email, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    	#gc = gspread.login(email, password)
    credentials = ServiceAccountCredentials.from_json_keyfile_name('pi-in-the-sky-13-ca776cc8e6db.json', scope)
    gc = gspread.authorize(credentials)
    sh = gc.create(spreadsheet)
    sh.share(EMAIL, perm_type='user', role='writer', notify=False)
    
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

    temp = sensor.read_temperature()
    pressure = sensor.read_pressure()
    altitude = sensor.read_altitude()

    tempStr = str(temp)
    pressureStr = str(pressure)
    altitudeStr = str(altitude)

    print ('Temperature: ' + str(temp) + ' C')
    print ('Pressure: ' + str(pressure) + ' Pa')
    print ('Altitude: ' + str(altitude) + ' m')

    #try:
    #json.dumps(my_dictionary, indent=4, sort_keys=True, default=str)

    fileWrite(getTime() + ", " + tempStr + ", " + pressureStr + ", " + altitudeStr + "\n")
    if(isOnline()):
        timeCheck = elapsed()
        while(pointer < len(getLine(-1)) and elapsed() - timeCheck < freq - 0.5 and isOnline()): 
            data = getLine(pointer).split(", ")
            worksheet.append_row((str(data[0]), str(data[1]), str(data[2]), str(data[3])))
            print ('Wrote a row to ' + NAME + '\n')
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
