from flask import Flask
from flask import render_template
##from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config.from_object('config')
##db = SQLAlchemy(application)

from app import views

##, models



