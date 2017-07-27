from flask import Flask, render_template, session, redirect, request, url_for, g
import os
from functools import wraps
from models import UserData

app = Flask(__name__)

userdata = []
app.secret_key = os.urandom(10)

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
		
	if request.method == 'GET':
		return render_template("signup.html")

	elif request.method == 'POST':
		name = request.form.get('inputName')
		password = request.form.get('inputPassword')
		email = request.form.get('inputEmail')
		username = request.form.get('inputuserName')

		userdata.append(UserData(name, password, email, username))
		return redirect(url_for("login"))

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	
	elif request.method == 'POST':
		for value in userdata:
			email = request.form.get('email')
			password = request.form.get('password')
			if value.email == email and value.password == password:
				session['email'] = value.email
				return redirect(url_for("goals"))

@app.route('/goals', methods=['GET', 'POST'])
def goals():
	return render_template('goals.html')

if __name__ == '__main__':
    app.run(debug=True)