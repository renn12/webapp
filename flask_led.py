from flask import Flask # /usr/lib/python2.7/dist-packages/flask
import RPi.GPIO as GPIO

app = Flask(__name__) # make instance

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route('/LED/ON')
def led_on():
	GPIO.output(8, GPIO.HIGH)
	return 'LED ON<br/><a href="/LED/OFF">LED OFF</a>'

@app.route('/LED/OFF')
def led_off():
	GPIO.output(8, GPIO.LOW)
	return 'LED OFF<br/><a href="/LED/ON">LED ON</a>'


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8888)
