import serial
import time

def readTemp():
  ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
  ser.flush()
  temp = ser.readline().decode('utf-8')
  return temp
