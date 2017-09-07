import Adafruit_DHT
import httplib, urllib, time

sensor = Adafruit_DHT.DHT11
pin = 14

def dht11_read():
	#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	temperature = Adafruit_DHT.read_retry(sensor, pin)[1]
	if temperature is not None:
		print('Temp={0:0.1f}*'.format(temperature))
		return temperature
	else:
		print('Failed to get reading. Try again!')
		return 0

while True:
	temp = dht11_read()
	print(temp)
	time.sleep(3)
