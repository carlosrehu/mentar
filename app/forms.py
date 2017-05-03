from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, PasswordField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

## this class will be called by the signup function in the views.py
## use the flask form functionalities and create variable names based on the input fields.
class SignupForm(Form):
    firstname = StringField("First Name", validators = [ DataRequired("Please enter your name.")])
    lastname = StringField("Last Name", validators = [ DataRequired("Please enter your last name.")])
    email = EmailField("Email", validators = [ DataRequired("Please enter your email address.")])
    gender = StringField("Gender")
    major = SelectField('Major', validators = [ DataRequired("Please select your major.")])
    minor = SelectField('Minor')
    age = IntegerField("Age", validators = [ DataRequired("Please enter a valid age.")])
    username = StringField("Username", validators = [ DataRequired("Please enter a valid username.")])
    password = PasswordField("Password", validators = [ DataRequired("Please create a password.")])
    phonenumber = StringField("Phone Number")
    profiletype = SelectField('Profile Type', validators = [ DataRequired("Please select a valid profile type.")])
    graddate = StringField("Graduation Date", validators = [ DataRequired("Please enter a valid graduation date.")])
    profession = StringField("Profession")
    aboutme = StringField("Tell us about yourself.")
    interests = StringField("What are your professional interets?")
    skills = StringField("Skills")
    city = StringField("City")
    state = StringField("State")

##  submit button
    submit = SubmitField("Submit")

    

##  class will be used by the views.py to get an tip for a student. This provides a flask text area
##  and will be displayed in the HTML file. This text area can be resized. 
class InterviewTips(Form):
    tip = StringField("Tip" ,widget=TextArea())

    submit = SubmitField("Submit")


##   Used by the views.py file to write jobs into the data table same idea as the previous classes from this file
class alumniJobs(Form):
    job = StringField("Job" ,widget=TextArea())

    submit = SubmitField("Submit")


##  Although only one variable is used, future iterations will call the answer variable to post the answer into
##  a separate table and create a one to many relationship of questions and answers. 
class PostAQuestion(Form):

    question = StringField("Question", widget=TextArea())

    answer = StringField("Answer", validators = [ DataRequired("Please type a response.")])

    submit = SubmitField("Submit")
