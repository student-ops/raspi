import serial, sys
port = "/dev/ttyUSB0"
baudrate = 115200
ser = serial.Serial(port, baudrate, timeout=0.1)
while True:
    data = ser.read(1)
    if data:
        data += ser.read(ser.inWaiting())
        sys.stdout.write(data.decode())
        sys.stdout.flush()
