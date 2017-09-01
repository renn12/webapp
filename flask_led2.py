from flask import Flask # /usr/lib/python2.7/dist-packages/flask
import RPi.GPIO as GPIO

app = Flask(__name__) # make instance

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route('/LED/<m>')
def led(m):
	if m == 'ON':
		GPIO.output(8, GPIO.HIGH)
	elif m == 'OFF':
		GPIO.output(8, GPIO.LOW)
	return 'LED %s' % m


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8888)
