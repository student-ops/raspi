import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)
GPIOsetup(25,GPIO.OUT)

while True:
    GPIO.output(25,GPIO.HIGH)
    sleep(0.8)
    GPIO.output(25,GPIO.LOW)
    sleep(0.8)
