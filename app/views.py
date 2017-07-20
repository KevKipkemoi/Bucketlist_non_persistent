from flask import Flask, request, render_template, flash, redirect, url_for
from flask_login import (LoginManager, login_required, login_user,
                         current_user, logout_user, UserMixin)
from functools import wraps
from flask import g, request, redirect, url_for
from app import SignUpForm, LoginForm, EditForm
from app import GoalsForm
from app import app, session, lm


@app.before_request
def before_request():
    g.user = current_user

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def index():
    return render_template('index.html')

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')


@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    form = LoginForm(request.form)
    if form.validate():
        if form.email.data == form.email.data:
            return redirect(url_for('viewentries'))
    else:
        flash_errors(form)
        print("Sign Up")
    return render_template('login.html', form=form)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    return render_template("index.html")


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.firstname.data, form.lastname.data, form.username.data, form.email.data,
                    form.password.data)
        return redirect(url_for('login'))
    else:
        flash_errors(form)
    return render_template('signup.html', form=form)


@app.route("/setgoals", methods=['POST', 'GET'])
@login_required
def setgoals():

    form = GoalsForm(request.form)
    if request.method == 'POST' and form.validate():
        new = Goals(form.body.data, form.tags.data, current_user_id)
        flash('Goal added')
        return redirect("viewentries/")
    else:
        flash_errors(form)
    return render_template('goals.html', form = form)

@app.route("/viewentries/<id>", methods=['GET'])
@app.route("/viewentries/", methods=['GET'])
@login_required
def viewentries(id=None):
    for entry in entry_rows:
        entries.append({
            "id": entry.id,
            "body": entry.body,
            "tags": entry.tags
        })
    return render_template('viewentries.html', entries=entries)
    
@app.route("/edit/<id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    form = EditForm(obj= goals)
    if request.method == 'POST' and id == id:
        goals.body = form.body.data
        goals.tags = form.tags.data
        flash('Goal reviewed')
        return redirect(url_for('viewentries', Goals.id == id))
    else:
        flash_errors(form)
    return render_template('edit.html', form=form)

