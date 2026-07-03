#SOS ... --- ...

import RPi.GPIO as GPIO
from time import sleep

LED = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW) 

def flash(led, duration):
    GPIO.output(led, True)
    sleep(duration)
    GPIO.output(led, False)
    sleep(duration)

while True:
    flash(LED, 0.2)
    flash(LED, 0.2)
    flash(LED, 0.2)
    sleep(0.3)
    
    flash(LED, 0.5)
    flash(LED, 0.5)
    flash(LED, 0.5)
    sleep(0.3)
    
    flash(LED, 0.2)
    flash(LED, 0.2)
    flash(LED, 0.2)
    sleep(1)