import sys
import urllib.request as urllib2
from time import sleep
import adafruit_dht
import board

dht_device = adafruit_dht.DHT11(board.D18)

#API key
myAPI = '6INNETAFAJ0FVX75'

baseURL = 'http://api.thingspeak.com/update?api_key=%s' % myAPI

def DHT11_data():
    #Reads the sensor
    temperature = dht_device.temperature
    humidity = dht_device.humidity
    return temperature, humidity

while True:
            try:
                temp, humi = DHT11_data()
                #temperature = dht_device.temperature
                #humidity = dht_device.humidity
                
                #Add format of two decimal places
                humi = '%.2f' % humi
                temp = '%.2f' % temp
            
            
                print("Humidity: %s, Temperature: %s " % (humi, temp))
                
       
                sleep(3)
                
            except RuntimeError as error:
                print(error.args[0])
             