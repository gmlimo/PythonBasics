import RPi.GPIO as GPIO
from time import sleep

LED1 = 13
LED2 = 15

#Pin configuration
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(LED1, GPIO.OUT, initial = GPIO.LOW) 
GPIO.setup(LED2, GPIO.OUT, initial = GPIO.LOW)

counter = 0
    
while True:
    if counter %2 == 0:
        led1 = LED1
        led2 = LED2
    else:
        led1 = LED2
        led2 = LED1
        
    GPIO.output(led1, True)
    GPIO.output(led2, False)
    sleep(1)
    counter = counter + 1