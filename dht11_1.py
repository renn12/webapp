import RPi.GPIO as GPIO
from DHT11_Python.dht11 import DHT11
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #pin number
GPIO.cleanup()

while True:
	instance = DHT11(pin = 8)
	result = instance.read()

	if result.is_valid():
		print("Temperature: %d C" % result.temperature)
		print("Humidity: %d" % result.humidity)
	else:
		print("Error: %d" % result.error_code)
	time.sleep(1)
