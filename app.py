from flask import Flask
import os
import sys
sys.path.append(os.getcwd())
from app import views

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
