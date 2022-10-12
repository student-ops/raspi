import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)


try:
while True:
    if GPIO.input(24) == GPIO.HIGH:
        GPIO.output(25,GPIO.HIGH)
    else:
        GPIO.output(25,GPIO.LOW)
    sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()