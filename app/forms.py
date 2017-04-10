from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class SignupForm(Form):
    firstname = StringField("First Name")
    lastname = StringField("Last Name")
    email = EmailField("Email")
    gender = StringField("Gender")
    major = SelectField('Major')
    minor = SelectField('Minor')
    age = IntegerField("Age")
    username = StringField("Username")
    password = StringField("Password")
    phonenumber = StringField("Phone Number")
    profiletype = SelectField('Profile Type')
    graddate = StringField("Graduation Date")
    profession = StringField("Profession")
    aboutme = StringField("Tell us about yourself.")
    interests = StringField("What are your professional interets?")
    skills = StringField("Skills")
    city = StringField("City")
    state = StringField("State")

    
    

    submit = SubmitField("Submit")

