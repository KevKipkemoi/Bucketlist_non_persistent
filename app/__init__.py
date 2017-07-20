from flask import Flask, request, render_template, flash, session, redirect, url_for
from flask_login import LoginManager
from app.forms import SignUpForm, LoginForm, EditForm
from app.forms import GoalsForm

lm = LoginManager()
lm.init_app(app)
lm.login_view = "login"

from app import views, models
