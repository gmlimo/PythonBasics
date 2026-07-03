import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #To use the pins as they apperar numbered
GPIO.setup(12, GPIO.OUT, initial = GPIO.LOW) #Pin 12 represents GPIO 18 in BCM mode

while True:
    GPIO.output(12, True)
    sleep(1)
    GPIO.output(12, False)
    sleep(1)