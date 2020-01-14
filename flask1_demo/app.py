from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
	a = 1
	b = 0
	c = a/b
	return "hello world"


if __name__ == '__main__':
	app.run(debug=True)