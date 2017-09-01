import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

TRIG = 12
ECHO = 16

GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)


try:
    while 1:
        #Trig Start
        GPIO.output(TRIG, True)
        time.sleep(0.5)
        GPIO.output(TRIG, False)

        #Echo Start
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time() #connect to echo pin

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print "Distance: ", distance, "cm"
	if distance > 7:
		os.system('curl http://192.168.0.124:8888/LED/ON')
	else:
		os.system('curl http://192.168.0.124:8888/LED/OFF')

except KeyboardInterrupt:
    pass
GPIO.cleanup()

