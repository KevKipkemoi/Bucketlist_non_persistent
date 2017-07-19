from app import db
from sqlalchemy import Column, ForeignKey, Integer, DateTime
from werkzeug.security import generate_password_hash, \
     check_password_hash
from sqlalchemy.orm import relationship
from passlib.hash import sha256_crypt
from flask_login import UserMixin
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite:///goals.db', echo = True)
Base = declarative_base() 

class User(UserMixin, Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.datetime.utcnow)
    updated_on = db.Column(db.DateTime)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


    def __init__(self, firstname, lastname, username, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        '''
        hashing the password
        '''
        self.pw_hash = generate_password_hash(password)


class Goals(Base):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.datetime.utcnow)
    updated_on = db.Column(db.DateTime)
    body = db.Column(db.String(1500), nullable=False)
    tags = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    jour = db.relationship('User')


    def __init__(self, body, tags, user_id):
        self.body = body
        self.tags = tags
        self.user_id = user_id


    def __repr__(self):
        return '<Goals %r>' % self.body

Base.metadata.create_all(engine)
