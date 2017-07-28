from flask import Flask, render_template, session, redirect, request, url_for
import os
from models import UserData
from bucket import Bucket

app = Flask(__name__)

userdata = []
app.secret_key = os.urandom(10)
error = None

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':		
		return render_template('signup.html')

	if request.method == 'POST':	
		name = request.form.get('inputName')
		password = request.form.get('inputPassword')
		email = request.form.get('inputEmail')
		username = request.form.get('inputuserName')
		new_user = UserData(name, username, email, password)
		userdata.append(new_user)

	return redirect(url_for("login"))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html")
		
	if request.method == 'POST':
		email = request.form['inputEmail']
		password = request.form.get('inputPassword')
		print(userdata)
		for value in userdata:
			if value.email == email and value.password == password:
				session['email'] = value.email
				return redirect(url_for("bucketlist"))
	return render_template("login.html")

@app.route('/bucketlist', methods=['GET', 'POST'])
def bucketlist():
	if session:
		if request.method == "GET":					
			return render_template("bucketlist.html")
		elif request.method == 'POST':
			description = request.form.get('addDescription')
			bucketlist = request.method.get('addBucketlist')
			user_bucket = Bucket.create_bucketlist(description, bucketlist)
			Bucket.data.append({
				value.email: user_bucket
			})

		for value in Bucket.data:
			print(value.description)
			print(value.bucketlist)
	else:
		return redirect(url_for("login"))

@app.route('/logout')
def logout():
	return redirect(url_for("index"))
	session.pop(session['email'])	

if __name__ == '__main__':
    app.run(debug=True)