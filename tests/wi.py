import serial

if __name__ == '__main__':
  ser = serial.Serial('/dev/ttyUSB0',115200)
  print(ser.name)
  ser.write(b'#?\n')
  ser.close()
