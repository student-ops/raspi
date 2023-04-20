import serial
import time

if __name__ == '__main__':
  ser = serial.Serial('/dev/ttyUSB0',115200,timeout =5)
  print(ser.name)
  program = b'#?\r'
  ser.write(program)
  time.sleep(0.1)
  result = ser.read_all()
  print(result)
  ser.close()

