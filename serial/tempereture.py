import serial
import time

if __name__ == '__main__':
  ser = serial.Serial('/dev/ttyACMO',9600,timeout=1)
  ser.flush()
  while(True):
    time.sleep(1)
    temp = ser.readline().decode('utf-8')
    print(temp)