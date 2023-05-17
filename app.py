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

@app.route("/list", methods=['POST', 'GET'])
def list():
  if request.method == 'POST':
    num = int(request.form['num'])
    num2 = int(request.form['name'])
    plus = num + num2
    minus = num - num2
    div = num * num2
    times = num / num2
    return render_template("list.html", plus=plus, minus=minus, div=div, times=times)

  else:
    return render_template("list.html")

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)