from app import application
from app import forms
from flask import render_template


@application.route('/')
@application.route('/aboutus.html')
def aboutus():
    return render_template('/aboutus.html')

@application.route('/alumniconnection.html')
def alumniconnection():
    return render_template('/alumniconnection.html')

@application.route('/contactus.html')
def contactus():
    return render_template('/contactus.html')

@application.route('/cquestions.html')
def cquestions():
    return render_template('/cquestions.html')

@application.route('/createprofile.html')
def createprofile():
    return render_template('/createprofile.html', form = SignupForm(), page_title = 'Signup to Bio Application')

@application.route('/experience.html')
def experience():
    return render_template('/experience.html')

@application.route('/homepage.html')
def homepage():
    return render_template('homepage.html')

@application.route('/interviewtipsstudent.html')
def interviewtipsstudent():
    return render_template('interviewtipsstudent.html')

@application.route('/javaquestions.html')
def javaquestions():
    return render_template('javaquestions.html')

@application.route('/postaquestion.html')
def postaquestion():
    return render_template('postaquestion.html')

@application.route('/practicequestions.html')
def practicequestions():
    return render_template('practicequestions.html')

@application.route('/studentmainpage.html')
def studenttmainpage():
    return render_template('studenttmainpage.html')







