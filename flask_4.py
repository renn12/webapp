from flask import Flask, request

app = Flask(__name__) #make instance

@app.route('/')
def index():
	return 'Method used: %s' % request.method

@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
	if request.method == 'GET':
		return 'You are using GET'
	elif request.method == 'POST':
		return 'You are probably using POST'
	else:
		return 'else'
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8888)
