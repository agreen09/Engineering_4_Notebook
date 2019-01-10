#original code by Dr. Shields
import time
import socket
import os

ipaddr = "---.---.---.---"
online = False

while not online:
    gw = os.popen("ip -4 route show default").read().split()
    if(len(gw) > 0):
        online = True
    if(online):
        print("Connected")
    else:
        print("Not online")
    time.sleep(1)
