import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)
GPIOsetup(2,GPIO.IN)


while True:
    if GPIO.LOW:
        print("somthing cencered")
        sleep(0.8)
    else:
        print("uncencerd")
        sleep(0.8)



