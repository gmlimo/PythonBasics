import Adafruit_DHT as dht
from time import sleep

try:
    while True:
        print("Reading Data...")
        humidity, temperature = dht.read_retry(dht.DHT22, 18)
        print("Temperature {0:0.1f} *C, Humidity {1:0.1f}".format(temperature, humidity))
        sleep(3)
        
except KeyboardInterrupt: #The program will be interrupted by a keyboard struck
    pass
    