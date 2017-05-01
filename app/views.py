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
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('homepage.html', forms=forms, name=name, profile=profile)
        else:
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
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('aboutus.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
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



##    stored_tip = []
##
##    for tip in cur:
##        stored_tip.append(tip)
##        print(tip)

    if request.method == 'POST':
        if forms.validate() == False:
            flash('AN INTERVIEW TIP IS REQUIRED')
            return render_template('alumnipostquestion.html')
        else:
            cur.execute(""" INSERT INTO interview_tips(tips) VALUES(%s)""", [forms.tip.data])
            interviewTips = cur.fetchall()
            forms.stored_tip = [(row[1], row[1]) for row in interviewTips ]
            conn.commit
            conn.autocommit(True)
            return redirect(url_for('alumnipostquestion'))
    if request.method == 'GET':

##        cur.execute("SELECT tips FROM interview_tips")
        cur.execute(""" SELECT tips FROM interview_tips """)
        stored_tip = cur.fetchall()
        cur.execute("SELECT f_name FROM user")
        name =  cur.fetchone()
        cur.execute("SELECT profile_type FROM user")
        profile = cur.fetchone()

        return render_template('alumnipostquestion.html', forms=forms, items=stored_tip, name=name, profile = profile)


@application.route('/careeropportunities')
def careeropportunities():
        if request.method == 'GET':
            if 'username' in session:
                username=session['username']
                cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                name =  cur.fetchone()
                cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                profile = cur.fetchone()

                return render_template('careeropportunities.html', forms=forms, name=name, profile=profile)
            else:
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
                cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                name =  cur.fetchone()
                cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                profile = cur.fetchone()

                return render_template('cplusquestions.html', forms=forms, name=name, profile=profile)
            else:
                return redirect(url_for('signin'))
        return render_template('cplusquestions.html')

@application.route('/cquestions')
def cquestions():
            if request.method == 'GET':
                if 'username' in session:
                    username=session['username']
                    cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                    name =  cur.fetchone()
                    cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                    profile = cur.fetchone()

                    return render_template('cquestions.html', forms=forms, name=name, profile=profile)
                else:
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
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('csharpquestions.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
        return render_template('csharpquestions.html')

@application.route('/experiences')
def experiences():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('experiences.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
        return render_template('experiences.html')

@application.route('/internships')
def internships():
        if request.method == 'GET':
            if 'username' in session:
                username=session['username']
                cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                name =  cur.fetchone()
                cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                profile = cur.fetchone()

                return render_template('internships.html', forms=forms, name=name, profile=profile)
            else:
                return redirect(url_for('signin'))
            return render_template('internships.html')

@application.route('/partfulltime', methods=['POST', 'GET'])
def partfulltime():
    # if request.method == 'GET':
    #     if 'username' in session:
    #         username=session['username']
    #         cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
    #         name =  cur.fetchone()
    #         cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
    #         profile = cur.fetchone()
    #
    #         return render_template('partfulltime.html', forms=forms, name=name, profile=profile)
    #     else:
    #         return redirect(url_for('signin'))
    #     return render_template('partfulltime.html')


    forms =  alumniJobs(request.form)

    #Post Method
    if request.method == 'POST':
        if forms.validate() == False:
            flash('A JOB IS REQUIRED')
            return render_template('partfulltime.html')
        else:
            cur.execute(""" INSERT INTO alumnijobs(job) VALUES(%s)""", [forms.job.data])
            alumnijobs = cur.fetchall()
            forms.stored_job = [(row[1], row[1]) for row in alumnijobs ]
            conn.commit
            conn.autocommit(True)
            return redirect(url_for('partfulltime'))

    #Get method
    if request.method == 'GET':

         if 'username' in session:
             username=session['username']
##        cur.execute("SELECT job FROM job_id")
             cur.execute(""" SELECT job FROM alumnijobs """)
             stored_job = cur.fetchall()
             cur.execute("SELECT f_name FROM user WHERE user_name = %s""", [username])
             name =  cur.fetchone()
             cur.execute("SELECT profile_type FROM user WHERE user_name = %s""", [username])
             profile = cur.fetchone()

             return render_template('partfulltime.html', forms=forms, items=stored_job, name=name, profile = profile)
         return render_template('partfulltime.html')



@application.route('/internationalstudentsposts')
def internationalstudentsposts():
        if request.method == 'GET':
            if 'username' in session:
                username=session['username']
                cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                name =  cur.fetchone()
                cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                profile = cur.fetchone()

                return render_template('internationalstudentsposts.html', forms=forms, name=name, profile=profile)
            else:
                return redirect(url_for('signin'))
            return render_template('internationalstudentsposts.html')

@application.route('/alumnijobpost', methods = ['POST', 'GET'])
def alumnijobpost():

    forms =  alumniJobs(request.form)

    #Post Method
    if request.method == 'POST':
        if forms.validate() == False:
            flash('A JOB IS REQUIRED')
            return render_template('alumnijobpost.html')
        else:
            cur.execute(""" INSERT INTO alumnijobs(job) VALUES(%s)""", [forms.job.data])
            alumnijobs = cur.fetchall()
            forms.stored_job = [(row[1], row[1]) for row in alumnijobs ]
            conn.commit
            conn.autocommit(True)
            return redirect(url_for('alumnijobpost'))



    #Get method
    if request.method == 'GET':
         if 'username' in session:
             username=session['username']
##        cur.execute("SELECT job FROM job_id")
             cur.execute(""" SELECT job FROM alumnijobs """)
             stored_job = cur.fetchall()
             cur.execute("SELECT f_name FROM user WHERE user_name = %s""", [username])
             name =  cur.fetchone()
             cur.execute("SELECT profile_type FROM user WHERE user_name = %s""", [username])
             profile = cur.fetchone()

             return render_template('alumnijobpost.html', forms=forms, items=stored_job, name=name, profile = profile)
         return render_template('alumnijobpost.html')

@application.route('/interviewtipsstudent')
def interviewtipsstudent():
            if request.method == 'GET':
                if 'username' in session:
                    username=session['username']
                    cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                    name =  cur.fetchone()
                    cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                    profile = cur.fetchone()

                    return render_template('interviewtipsstudent.html', forms=forms, name=name, profile=profile)
                else:
                    return redirect(url_for('signin'))
                return render_template('interviewtipsstudent.html')

@application.route('/javaquestions')
def javaquestions():
            if request.method == 'GET':
                if 'username' in session:
                    username=session['username']
                    cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                    name =  cur.fetchone()
                    cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                    profile = cur.fetchone()

                    return render_template('javaquestions.html', forms=forms, name=name, profile=profile)
                else:
                    return redirect(url_for('signin'))
                return render_template('javaquestions.html')

@application.route('/javascriptquestions')
def javascriptquestions():
            if request.method == 'GET':
                if 'username' in session:
                    username=session['username']
                    cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                    name =  cur.fetchone()
                    cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                    profile = cur.fetchone()

                    return render_template('javascriptquestions.html', forms=forms, name=name, profile=profile)
                else:
                    return redirect(url_for('signin'))
                return render_template('javascriptquestions.html')

@application.route('/phpquestions')
def phpquestions():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('phpquestions.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
        return render_template('phpquestions.html')

@application.route('/postaquestion', methods=['GET', 'POST'])
def postaquestion():

    forms =  PostAQuestion(request.form)

##    quesans = cur.execute(""" SELECT quesans FROM mentarquestions """)
##    quesans = cur.fetchall()


    if request.method == 'POST':
            if forms.question.data != None:
                cur.execute(""" INSERT INTO mentarquestions(quesans) VALUES(%s)""", [forms.question.data])
            #print "cur.execute(''' INSERT INTO questions(question) VALUES(%s)''', (forms.question.data))"
                conn.commit
                conn.autocommit(True)
            #cur.execute(""" INSERT INTO answers(answer, question_id) VALUES(%s, %s)""", [forms.answer.data], questionid)
##            interviewTips = cur.fetchall()
##            forms.stored_tip = [(row[1], row[1]) for row in interviewTips ]
            if forms.answer.data != None:
                cur.execute(""" INSERT INTO answers(answer) VALUES(%s)""", [forms.answer.data])
                conn.commit
                conn.autocommit(True)

            return redirect(url_for('postaquestion'))
    if request.method == 'GET':
##
        #cur.execute("SELECT tips FROM interview_tips")
##
        print "Do i Get here?"
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()


            print username
##        return render_template('alumnipostquestion.html', forms=forms, items=stored_tip, name=name, profile = profile)cur.execute("SELECT f_name, l_name, email, gender, major, minor, age, user_name, password, phone_number, profile_type, graduate_date, profession, about_me, interests, skills, city, state FROM user WHERE user_name = %s", [username])

##                    data = cur.fetchone()

            questiontest = cur.execute(""" SELECT quesans FROM mentarquestions """)
            questiontest = cur.fetchall()
            answer = cur.execute(""" SELECT answer FROM answers """)
            answer = cur.fetchall()

        #answertest = cur.execute(""" SELECT question FROM answers LEFT JOIN questions ON answers.answer_id = question_id  """)
        #answertest = cur.fetchall()
            return render_template('postaquestion.html', forms=forms, name=name, profile=profile, question=questiontest)
        else:
            return redirect(url_for('signin'))
    return render_template('postaquestion.html')

@application.route('/practicequestions')
def practicequestions():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('practicequestions.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('practicequestions.html')

@application.route('/practicequestionsbiology')
def practicequestionsbiology():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('practicequestionsbiology.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('practicequestionsbiology.html')

@application.route('/practicequestionsbusiness')
def practicequestionsbusiness():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('practicequestionsbusiness.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('practicequestionsbusiness.html')

@application.route('/practicequestionsgeneral')
def practicequestionsgeneral():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('practicequestionsgeneral.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('practicequestionsgeneral.html')

@application.route('/practicequestionsmath')
def practicequestionsmath():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('practicequestionsmath.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('practicequestionsmath.html')

@application.route('/profilepage', methods=['GET', 'POST'])
def profilepage():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('profilepage.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('profilepage.html')

@application.route('/pythonquestions')
def pythonquestions():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('pythonquestions.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('pythonquestions.html')

@application.route('/rubyquestions')
def rubyquestions():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('rubyquestions.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('rubyquestions.html')


@application.route('/sqlquestions')
def sqlquestions():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('sqlquestions.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
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
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('typeofquestions.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('typeofquestions.html')

@application.route('/verbalquestions')
def verbalquestions():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('verbalquestions.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('verbalquestions.html')

@application.route('/underconstruction')
def underconstruction():
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('underconstruction.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
            return render_template('underconstruction.html')
