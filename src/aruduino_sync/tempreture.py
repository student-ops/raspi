import serial
import time

def readTemp():
  sum = 0
  ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
  ser.flush()
  _ = ser.readline().decode('utf-8')
  for i in range(5):
    sum += float(ser.readline().decode('utf-8'))
    if(i==0):
      continue
    time.sleep(1)
  return sum/5
