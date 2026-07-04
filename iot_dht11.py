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
        #If reading is valid
        if float(temp) and float(humi):
            
            #Add format of two decimal places
            humi = '%.2f' % humi
            temp = '%.2f' % temp
            
            #Sending the data to thingspeak
            conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (temp, humi))
            print(conn.read())
            #close the connection
            conn.close()
            print("Humidity: %s, Temperature: %s " % (humi, temp))
        else:
            print('Error')
        #DHT11 requieres 2 seconds to give a reading    
        sleep(3)
    except:
         break
             