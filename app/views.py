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

@application.route('/cplusquestions.html')
def cplusquestions():
    return render_template('/cplusquestions.html')

@application.route('/cquestions.html')
def cquestions():
    return render_template('/cquestions.html')

@application.route('/createprofile.html')
def createprofile():
    return render_template('/createprofile.html', form = SignupForm(), page_title = 'Signup to Bio Application')

@application.route('/csharpquestions.html')
def csharpquestions():
    return render_template('/csharpquestions.html')

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

@application.route('/javascriptquestions.html')
def javascriptquestions():
    return render_template('javascriptquestions.html')

@application.route('/phpquestions.html')
def phpquestions():
    return render_template('phpquestions.html')

@application.route('/postaquestion.html')
def postaquestion():
    return render_template('postaquestion.html')

@application.route('/practicequestions.html')
def practicequestions():
    return render_template('practicequestions.html')

@application.route('/profilepage.html')
def profilepage():
    return render_template('profilepage.html')

@application.route('/pythonquestions.html')
def pythonquestions():
    return render_template('pythonquestions.html')

@application.route('/rubyquestions.html')
def rubyquestions():
    return render_template('rubyquestions.html')

@application.route('/sqlquestions.html')
def sqlquestions():
    return render_template('sqlquestions.html')

@application.route('/studentmainpage.html')
def studenttmainpage():
    return render_template('studenttmainpage.html')

@application.route('/verbalquestions.html')
def verbalquestions():
    return render_template('verbalquestions.html')







