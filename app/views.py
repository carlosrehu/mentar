from app import application
import MySQLdb
from app import forms
from flask import *
from forms import SignupForm



conn = MySQLdb.connect(host="localhost",
                       user = "root",
                       passwd = "raspberry",
                       db = "mentar")

cur = conn.cursor()


@application.route('/')
@application.route('/homepage')
def homepage():
    return render_template('homepage.html')

@application.route('/aboutus', methods = ['GET'])
def aboutus():

    if request.method == 'GET':
        return render_template('aboutus.html')

@application.route('/alumniconnection')
def alumniconnection():
    return render_template('alumniconnection.html')

@application.route('/contactus')
def contactus():
    return render_template('contactus.html')

@application.route('/cplusquestions')
def cplusquestions():
    return render_template('cplusquestions.html')

@application.route('/cquestions')
def cquestions():
    return render_template('cquestions.html')

@application.route('/createprofile', methods = ['POST', 'GET'])
def createprofile():
    forms = SignupForm()

    cur.execute(""" SELECT * FROM degrees ORDER BY degree_type """)
    major_data = cur.fetchall()
    print major_data
    forms.major.choices = [(row [1], row[1]) for row in major_data ]

    cur.execute(""" SELECT * FROM degrees WHERE minor = 1 ORDER BY degree_type ASC """)
    minor_data = cur.fetchall()
    forms.minor.choices = [(row[1], row[1]) for row in minor_data ]

    cur.execute(""" SELECT * FROM profile_type ORDER BY type ASC """)
    profile_data = cur.fetchall()
    forms.profiletype.choices = [(row[1], row[1]) for row in profile_data ]

    if request.method == 'POST':
        if forms.validate() == False:
            flash('ALL FIELDS ARE REQURIED')
            return render_template('createprofile.html', forms = forms)
        else:
            print "cur.execute(''' INSERT INTO users ( major) values(%s)''', (forms.major.data))", "db.commit", "db.autocommit(True)", forms.major.data
            return redirect(url_for('homepage.html'))
    elif request.method == 'GET':
        return render_template('createprofile.html', forms = forms)

@application.route('/csharpquestions')
def csharpquestions():
    return render_template('csharpquestions.html')

@application.route('/experience')
def experience():
    return render_template('experience.html')



@application.route('/interviewtipsstudent')
def interviewtipsstudent():
    return render_template('interviewtipsstudent.html')

@application.route('/javaquestions')
def javaquestions():
    return render_template('javaquestions.html')

@application.route('/javascriptquestions')
def javascriptquestions():
    return render_template('javascriptquestions.html')

@application.route('/phpquestions')
def phpquestions():
    return render_template('phpquestions.html')

@application.route('/postaquestion')
def postaquestion():
    return render_template('postaquestion.html')

@application.route('/practicequestions')
def practicequestions():
    return render_template('practicequestions.html')

@application.route('/profilepage')
def profilepage():
    return render_template('profilepage.html')

@application.route('/pythonquestions')
def pythonquestions():
    return render_template('pythonquestions.html')

@application.route('/rubyquestions')
def rubyquestions():
    return render_template('rubyquestions.html')

@application.route('/sqlquestions')
def sqlquestions():
    return render_template('sqlquestions.html')

@application.route('/studentmainpage')
def studenttmainpage():
    return render_template('studenttmainpage.html')

@application.route('/verbalquestions')
def verbalquestions():
    return render_template('verbalquestions.html')







