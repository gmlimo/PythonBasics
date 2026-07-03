from gpiozero import LED
from time import sleep

#Pins are in BCM mode meaning... the numbering is a GPIO18, GPIO17 and so on. 
led1 = LED(18)
led2 = LED(17)
led3 = LED(27)
led4 = LED(22)

sleeptime = 0.2

while True:
    led1.on()
    sleep(sleeptime)
    led1.off()
      
    led2.on()
    sleep(sleeptime)
    led2.off()
   
    led3.on()
    sleep(sleeptime)
    led3.off()
       
    led4.on()
    sleep(sleeptime)
    led4.off()
    