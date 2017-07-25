from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField,Form
#from flask.ext.pagedown.fields import PageDownField
from flask_pagedown.fields import PageDownField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = StringField('Email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(message='Must provide a password.')])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('Submit')

class SignUpForm(Form):
    firstname = StringField('firstname', [validators.Length(min=2, max=20)])
    lastname = StringField('lastname', [validators.Length(min=2, max=20)])
    username = StringField('Username', [validators.Length(min=2, max=25)])
    email = StringField('Email Address', [validators.Length(min=2, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords dono match')
    ])
    confirm = PasswordField('Renter Password')
    
   
class GoalsForm(Form):
    #id
    description = StringField('Description', [validators.Length(min=3, max=25)])
    body = PageDownField('Body', [validators.Length(min=1, max=1500)])
    tags = StringField('Tags', [validators.Length(min=1, max=20)])

class EditForm(Form):
    body = PageDownField('Body', [validators.Length(min=1, max=1500)])
    tags = StringField('Tags', [validators.Length(min=1, max=20)])


