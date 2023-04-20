import serial
import time

if __name__ == '__main__':

  ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=5)
  print(ser.name)

  # read program code from file and add \r to each line
  with open('display.txt', 'r') as f:
      program_lines = [line.strip() + '\r' for line in f.readlines()]
  program = ''.join(program_lines).encode()

  ser.write(b'edit 1')
  time.sleep(0.1)
  ser.write(program)
  ser.write(b'edit 0')
  time.sleep(0.1)
  ser.write(b'run')
  time.sleep(2)
  result = ser.readline()
  print(result)
  ser.close()