from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField,Form
#removed .ext. incase anything fails
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
    body = PageDownField('Body', [validators.Length(min=1, max=1500)])
    tags = StringField('Tags', [validators.Length(min=1, max=20)])

class EditForm(Form):
    body = PageDownField('Body', [validators.Length(min=1, max=1500)])
    tags = StringField('Tags', [validators.Length(min=1, max=20)])

class Bucket(dict, LoginForm, GoalsForm):

    def __init__(self, username, password, goal):
        self.username = username
        self.password = password
        self.goal = goal
    
    remember = False
    added_user = False
    
    def login(self, username):
        if username in user.keys():
            if password == users[username][0]:
                print('login successful')
                remember = True
                return remember
        else:
            print('invalid username or password')
            
    def add_user(self, username, password):
        if username not in users.keys():
            user[username] = [password]
            return 1

    def invalid_user(self, username, password):
        reset = 0
        if not login(username):
            self.users.update({username : [password]})
            added_user = True
            if added_user:
                reset = 1
                added_user = False
            return reset
                
        
    def display_goal(self, username):
        if remember:
            return self.user[username][1]
        else:
            print('please login/signup')
            
    def add_goal(self, username, goal):      
        if remember:
            self.user[username][1].insert(goal)
        else:
            print('please login/signup')
            
    def logout(self, username):
        remember = False
