from flask import Flask, request, render_template, flash, redirect, url_for
from flask_login import (LoginManager, login_required, login_user,
                         current_user, logout_user, UserMixin)
from functools import wraps
from flask import g, request, redirect, url_for
from forms import SignUpForm, LoginForm, EditForm
from app import GoalsForm

app = Flask(__name__)
current_users = {}


@app.route('/')
def index():
    return render_template('index.html')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
#@app.route(/add_goal)

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.firstname.data, form.lastname.data, form.username.data, form.email.data,
                    form.password.data)
        current_users[form.email.data]: user
        flash('Account Created')
        return redirect(url_for('login'))
    else:
        flash_errors(form)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)