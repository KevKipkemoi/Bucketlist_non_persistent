from flask import Flask, render_template, session, redirect, request, url_for
import os
from models import UserData

app = Flask(__name__)

userdata = []
app.secret_key = os.urandom(10)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
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
		return redirect(url_for("index"))

@app.route('/login')
def login():
	for value in userdata:
		if value.email == email and value.password == password:
			session['email'] = value.email
			return render_template("goals.html")

		else:
			return render_template("goals.html")

if __name__ == '__main__':
    app.run(debug=True)