from flask import Flask, render_template

 
app = Flask(__name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':

		return render_template("signup.html")

	if request.method == 'POST':
		name = reuqest.form.get('inputName')