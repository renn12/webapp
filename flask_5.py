from flask import Flask, render_template
app = Flask(__name__)

@app.route('/profile/<name>')
def profile(name):
	return render_template('profile.html', key = name)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8888)
