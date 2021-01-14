import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

pin = '4'

c = int(input("enter count number: "))

for i in range(1, c+1, 1):
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
    		print(i, 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
		time.sleep(2)
	else:
   		 print('Failed to get reading. Try again!')
