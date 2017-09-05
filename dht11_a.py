import Adafruit_DHT
import httplib, urllib, time

KEY = '76OX405LY0LT7B8Q'
headers = {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}

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
	params = urllib.urlencode({'field1': temp, 'key':KEY })
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
                conn.request("POST","/update",params, headers)
                response = conn.getresponse()
                print response.status, response.reason
                print "success"
        except:
                print "Connection failed"
        time.sleep(5)
