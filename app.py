from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route("/hello")
def hello():
	flash("what's your name?")
	return render_template("hello.html")

@app.route("/hello", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("hello.html")

@app.route("/count")
def count():
  return render_template("count.html")


if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)