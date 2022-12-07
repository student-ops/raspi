#!/usr/bin/env python3
import serial
import time
def readTempreture():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    ser.write(b"Hello from Raspberry Pi!\n")
    temp = ser.readline().decode('utf-8').rstrip()
    print(temp)
    return temp
