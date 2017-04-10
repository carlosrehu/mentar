from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class SignupForm(Form):
    firstname = StringField("First Name", validators = [ DataRequired("Please enter your name.")])
    lastname = StringField("Last Name", validators = [ DataRequired("Please enter your name.")])
    email = EmailField("Email", validators = [ DataRequired("Please enter your email address.")])
    username = StringField("Username", validators = [ DataRequired("Please enter a valid username.")])
    password = StringField("Password", validators = [ DataRequired("Please enter a password.")])
    city = StringField("City", validators = [ DataRequired("Please enter your city.")])
    state = StringField("State", validators = [ DataRequired("Please enter your state.")])
    profiletype = SelectField('Profile Type', validators = [ DataRequired("Select your profile type.")])
    major = SelectField('Major', validators = [ DataRequired("Select your major.")])
    minor = SelectField('Minor')
    graddate = StringField("Graduation Date", validators = [ DataRequired("Please enter your graduation date, or anticipated date of graduation.")])
    profession = StringField("Profession")
    interests = StringField("What are your professional interets?")
    skills = StringField("Skills")
    aboutme = StringField("Tell us about yourself.")

    submit = SubmitField("Submit")

