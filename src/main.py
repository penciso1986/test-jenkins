from flask import Flask
app = Flask(__name__)

def resta(a,b):
	return a-b

@app.route("/")
def hello():
	res = resta(10,20)
	return "Hello World %s" % (res)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
