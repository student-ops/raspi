import serial
from serial import Serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=3)

    print(ser.name)
    # read program code from file and add \r to each line
    with open('printtmp.txt', 'r') as f:
        program_lines = [line.strip() + '\r' for line in f.readlines()]
    program = ''.join(program_lines).encode()

    ser.write(b'edit 1 \r')
    time.sleep(0.1)
    ser.write(program)
    time.sleep(0.1)
    ser.write(b'edit 0 \r')
    time.sleep(0.1)
    ser.write(b'run \r')
    times = 0

    while True:
        result = ser.read(size=1000)
        if not result:
            times += 1
            print(str(times) + ":"+result.decode("utf-8"))
            continue
        else:
            print("hit")
            break

    print(result)
    ser.close()
