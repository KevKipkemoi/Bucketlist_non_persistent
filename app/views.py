from flask import Flask, render_template
from models import UserData

app = Flask(__name__)

userdata = []

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
def signup():
		
	return render_template("signup.html")
"""
	if request.method == 'POST':
		name = request.form.get('inputName')
		password = request.form.get('inputPassword')
		email = request.form.get('inputEmail')
		username = request.form.get('userName')

		userdata.append(models.UserData(name, password, email, username))
"""


if __name__ == '__main__':
    app.run(debug=True)