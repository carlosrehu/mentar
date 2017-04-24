from app import application
import MySQLdb
from app import forms
from flask import *
from forms import *
from flask import session
from hashlib import md5
import os



conn = MySQLdb.connect(host="localhost",
                       user = "root",
                       passwd = "raspberry",
                       db = "mentar")

cur = conn.cursor()
application.secret_key = os.urandom(32)

class ServerError(Exception):pass


@application.route('/')
@application.route('/homepage', methods = ['POST', 'GET'])
def homepage():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']

            cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

            data = cur.fetchone()
            print data
            print cur.fetchone()
            return render_template('homepage.html', items=data)

    return redirect(url_for('signin'))
    return render_template('homepage.html')

##    3session.clear()
##    3if 'username' in session:
##     3   return redirect(url_for('studentmainpage'))
##    error = None
##    try:
##        if request.method == 'POST':
##            username_form = request.form['username']
##            print username_form
##            cur.execute("SELECT COUNT(1) FROM user WHERE user_name = %s", [username_form])
##            if not cur.fetchone()[0]:
##                raise ServerError('Invalid username')
##            print cur.fetchone()
##            password_form = request.form['password']
##
##            cur.execute("SELECT password FROM user WHERE user_name = %s", [username_form])
##
##            for row in cur.fetchall():
##                if password_form == row[0]:
##                    session['username'] = request.form['username']
##
##                    return redirect(url_for('studentmainpage'))
##            raise ServerError('Invalid password')
##    except ServerError as e:
##        error = str(e)
##    return render_template('homepage.html')



@application.route('/aboutus', methods = ['GET'])
def aboutus():
    print session
    if 'username' not in session:


        return redirect(url_for('homepage'))
    else:
        return render_template('aboutus.html')

##3        return render_template('aboutus.html')

@application.route('/alumniconnection')
def alumniconnection():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']

            cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

            data = cur.fetchone()
            print data
            print cur.fetchone()
            return render_template('alumniconnection.html', items=data)

    return redirect(url_for('signin'))
    return render_template('alumniconnection.html')

@application.route('/alumnipostquestion', methods = ['POST', 'GET'])
def alumnipostquestion():

##    if 'username' in session:
##        name=session['username']
##        print name
##        return render_template('alumnipostquestion.html', username=name)
##    else:
##        return redirect(url_for('homepage'))

    forms =  InterviewTips(request.form)

    cur.execute(""" SELECT tips FROM interview_tips """)
    stored_tip = cur.fetchall()

##    stored_tip = []
##
##    for tip in cur:
##        stored_tip.append(tip)
##        print(tip)

    print stored_tip
    print "Testing??"
    if request.method == 'POST':
        if forms.validate() == False:
            flash('AN INTERVIEW TIP IS REQUIRED')
            return render_template('alumnipostquestion.html')
        else:
            cur.execute(""" INSERT INTO interview_tips(tips) VALUES(%s)""", [forms.tip.data])
            print "cur.execute(''' INSERT INTO interview_tips(tips) VALUES(%s)''', (forms.tip.data))"
            print "hmmm"
            interviewTips = cur.fetchall()
            forms.stored_tip = [(row[1], row[1]) for row in interviewTips ]
            conn.commit
            conn.autocommit(True)
            return redirect(url_for('alumnipostquestion'))
    if request.method == 'GET':

        cur.execute("SELECT tips FROM interview_tips")

        print "another test"

        print cur.fetchone()
        return render_template('alumnipostquestion.html', forms=forms, items=stored_tip)


@application.route('/careeropportunities')
def careeropportunities():
        if request.method == 'GET':
            if 'username' in session:
                username=session['username']

                cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

                data = cur.fetchone()
                print data
                print cur.fetchone()
                return render_template('careeropportunities.html', items=data)

        return redirect(url_for('signin'))
        return render_template('careeropportunities.html')

@application.route('/contactus')
def contactus():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']

            cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

            data = cur.fetchone()
            print data
            print cur.fetchone()
            return render_template('contactus.html', items=data)

    return redirect(url_for('signin'))
    return render_template('contactus.html')

@application.route('/cplusquestions')
def cplusquestions():
        if request.method == 'GET':
            if 'username' in session:
                username=session['username']

                cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

                data = cur.fetchone()
                print data
                print cur.fetchone()
                return render_template('cplusquestions.html', items=data)

        return redirect(url_for('signin'))
        return render_template('cplusquestions.html')

@application.route('/cquestions')
def cquestions():
            if request.method == 'GET':
                if 'username' in session:
                    username=session['username']

                    cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

                    data = cur.fetchone()
                    print data
                    print cur.fetchone()
                    return render_template('cquestions.html', items=data)

            return redirect(url_for('signin'))
            return render_template('cquestions.html')

@application.route('/createprofile', methods = ['POST', 'GET'])
def createprofile():
    forms = SignupForm(request.form)

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
        print forms.validate(), 'somemmmmm'
        if forms.validate() == False:
            flash('ALL FIELDS ARE REQURIED')
            return render_template('createprofile.html', forms = forms)
        else:
            cur.execute(""" INSERT INTO user(f_name, l_name, email, gender, major, minor,
                            age, user_name, password, phone_number, profile_type, graduate_date,
                            profession, about_me, interests, skills, city, state) VALUES(%s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                        ( forms.firstname.data, forms.lastname.data, forms.email.data, forms.gender.data,
                          forms.major.data, forms.minor.data, forms.age.data, forms.username.data,
                          forms.password.data, forms.phonenumber.data, forms.profiletype.data, forms.graddate.data,
                          forms.profession.data, forms.aboutme.data, forms.interests.data, forms.skills.data, forms.city.data, forms.state.data))
            conn.commit
            conn.autocommit(True)

            print "cur.execute(''' INSERT INTO users ( major) values(%s)''', (forms.major.data))", "db.commit", "db.autocommit(True)", forms.major.data
            return redirect(url_for('studentmainpage'))
    elif request.method == 'GET':
        return render_template('createprofile.html', forms = forms)



@application.route('/signinpage', methods=['GET', 'POST'])
def signin():
    session.clear()
    if 'username' in session:
        return redirect(url_for('homepage'))
    error = None
    try:
        if request.method == 'POST':
            username_form = request.form['username']
            cur.execute("SELECT COUNT(1) FROM user WHERE user_name = %s", [username_form])
            if not cur.fetchone()[0]:
                raise ServerError('Invalid username')
            print cur.fetchone()
            password_form = request.form['password']

            cur.execute("SELECT password FROM user WHERE user_name = %s", [username_form])

            for row in cur.fetchall():
                if password_form == row[0]:
                    session['username'] = request.form['username']

                    return redirect(url_for('homepage'))
            raise ServerError('Invalid password')
    except ServerError as e:
        error = str(e)
    return render_template('signinpage.html')

@application.route('/signout')
def signout():
    session.pop('username', None)
    session.clear()
    session.clear()
    return redirect(url_for('clearsession'))

@application.route('/clearsession')
def clearsession():
    session.clear()
    return redirect('homepage')

@application.route('/csharpquestions')
def csharpquestions():
    return render_template('csharpquestions.html')

##@application.route('/experience')
##def experience():
##    return render_template('experience.html')

@application.route('/internships')
def internships():
    return render_template('internships.html')

@application.route('/partfulltime')
def partfulltime():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']

            cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

            data = cur.fetchone()
            print data
            print cur.fetchone()
            return render_template('partfulltime.html', items=data)

    return redirect(url_for('signin'))
    return render_template('partfulltime.html')

@application.route('/internationalstudentsposts')
def internationalstudentsposts():
    return render_template('internationalstudentsposts.html')

@application.route('/alumnijobpost')
def alumnijobpost():
        if request.method == 'GET':
            if 'username' in session:
                username=session['username']

                cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

                data = cur.fetchone()
                print data
                print cur.fetchone()
                return render_template('alumnijobpost.html', items=data)

        return redirect(url_for('signin'))
        return render_template('alumnijobpost.html')

@application.route('/interviewtipsstudent')
def interviewtipsstudent():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']

            cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

            data = cur.fetchone()
            print data
            print cur.fetchone()
            return render_template('interviewtipsstudent.html', items=data)

    return redirect(url_for('signin'))
    return render_template('interviewtipsstudent.html')

@application.route('/javaquestions')
def javaquestions():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']

            cur.execute("SELECT f_name, FROM user WHERE user_name = %s", [username])

            data = cur.fetchone()
            print data
            print cur.fetchone()
            return render_template('javaquestions.html', items=data)

    return redirect(url_for('signin'))
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

@application.route('/practicequestionsbiology')
def practicequestionsbiology():
    return render_template('practicequestionsbiology.html')

@application.route('/practicequestionsbusiness')
def practicequestionsbusiness():
    return render_template('practicequestionsbusiness.html')

@application.route('/practicequestionsgeneral')
def practicequestionsgeneral():
    return render_template('practicequestionsgeneral.html')

@application.route('/practicequestionsmath')
def practicequestionsmath():
    return render_template('practicequestionsmath.html')

@application.route('/profilepage', methods=['GET', 'POST'])
def profilepage():

    if request.method == 'GET':
        if 'username' in session:
            username=session['username']

            cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])
##            cur.fetchone()


            data = cur.fetchone()
            print data
##            print test
##            print major_user, 'numer', firstname
##          print name
            print cur.fetchone()
            return render_template('profilepage.html', items=data)

    return redirect(url_for('signinpage'))

@application.route('/pythonquestions')
def pythonquestions():
    return render_template('pythonquestions.html')

@application.route('/rubyquestions')
def rubyquestions():
    return render_template('rubyquestions.html')

@application.route('/sqlquestions')
def sqlquestions():
    return render_template('sqlquestions.html')

@application.route('/studentmainpage', methods=['GET', 'POST'])
def studentmainpage():
    if 'username' in session:
        name=session['username']
        print name
        return render_template('studentmainpage.html', username=name)

    return redirect(url_for('homepage'))

@application.route('/studentconnection')
def studentconnection():
    return render_template('studentconnection.html')

@application.route('/typeofquestions')
def typeofquestions():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']

            cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

            data = cur.fetchone()
            print data
            print cur.fetchone()
            return render_template('typeofquestions.html', items=data)

    return redirect(url_for('signin'))
    return render_template('typeofquestions.html')

@application.route('/verbalquestions')
def verbalquestions():
    return render_template('verbalquestions.html')
