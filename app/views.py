from app import application
import MySQLdb
from app import forms
from flask import *
from forms import *
from flask import session
from hashlib import md5
import os


##create connection to the database
conn = MySQLdb.connect(host="localhost",
                       user = "root",
                       passwd = "raspberry",
                       db = "mentar")

cur = conn.cursor()
application.secret_key = os.urandom(32)

class ServerError(Exception):pass

##  create the base route (main index) for the web
@application.route('/')

## Create the base route for the homepage
@application.route('/homepage', methods = ['POST', 'GET'])
def homepage():

##  this will check whether or not the user in session is alreadi signed in. If the person is signed in
##  then the database will be accessed and the user's name and profile type will be displayed.
##  If the user is not in session, then the user will be sent to the signin page where s/he can create a profile
##  or sign in.
    if request.method == 'GET':
        if 'username' in session:
            ##assign the current user name to the username variable so we can retrieve information from the DB
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()
##          name and profile will be assigned to name and profile variables respectively. the latter variables
##          are the ones that will be called by the html files and display the requested data.
            return render_template('homepage.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
        return render_template('homepage.html')

@application.route('/aboutus', methods = ['GET'])
def aboutus():

##  Checks login session
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()

            return render_template('aboutus.html', name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
    return render_template('aboutus.html')



@application.route('/alumniconnection')
def alumniconnection():

##  Checks login session and assigns variables
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']

            cur.execute("SELECT f_name FROM user WHERE user_name = %s", [username])

            data = cur.fetchone()
            return render_template('alumniconnection.html', items=data)

    return redirect(url_for('signin'))
    return render_template('alumniconnection.html')

@application.route('/alumnipostquestion', methods = ['POST', 'GET'])
def alumnipostquestion():

##      FUNCTION UNDER CONSTRUCTION. WORKING ON MANAGING SESSIONS. SESSION VALIDATION WIL NEED TO BE
##      MOVED TO THE 'GET' STATEMENT AND LOG THE QUESTIONS TO THE USER

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
##  Checks login session and assigns variables
        if request.method == 'GET':
            if 'username' in session:
                username=session['username']
                cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                name =  cur.fetchone()
                cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                profile = cur.fetchone()

                return render_template('careeropportunities.html', name=name, profile=profile)
            else:
                return redirect(url_for('signin'))
        return render_template('careeropportunities.html')

@application.route('/contactus')
def contactus():

##  Checks login session and assigns variables
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("SELECT f_name FROM user WHERE user_name = %s", [username])
            data = cur.fetchone()
            print data
            print cur.fetchone()
            return render_template('contactus.html', items=data)

    return redirect(url_for('signin'))
    return render_template('contactus.html')

@application.route('/cplusquestions')
def cplusquestions():
##  Checks login session and assigns variables 
        if request.method == 'GET':
            if 'username' in session:
                username=session['username']
                cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                name =  cur.fetchone()
                cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                profile = cur.fetchone()
##              forms variable will be used in future iterations.
                return render_template('cplusquestions.html', forms=forms, name=name, profile=profile)
            else:
                return redirect(url_for('signin'))
        return render_template('cplusquestions.html')

@application.route('/cquestions')
def cquestions():

##  Checks login session and assigns variables
            if request.method == 'GET':
                if 'username' in session:
                    username=session['username']
                    cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                    name =  cur.fetchone()
                    cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                    profile = cur.fetchone()
##              forms variable will be used in future iterations.
                    return render_template('cquestions.html', forms=forms, name=name, profile=profile)
                else:
                    return redirect(url_for('signin'))
            return render_template('cquestions.html')

@application.route('/createprofile', methods = ['POST', 'GET'])
def createprofile():

    ## call the SignupForm class from the forms.py file and assigns it to the variable forms
    ## this forms variable will be hae access to the variables defined in the SignupForm class.
    forms = SignupForm(request.form)
    
    ## gather major information from the degrees table. 
    cur.execute(""" SELECT * FROM degrees ORDER BY degree_type """)
    major_data = cur.fetchall()
    
    ## create a flask list of major choices that will be displayed in the html file.
    forms.major.choices = [(row [1], row[1]) for row in major_data ]
    
    ## gather information from the degrees table and generate a choices list for the minor as well.
    cur.execute(""" SELECT * FROM degrees WHERE minor = 1 ORDER BY degree_type ASC """)
    minor_data = cur.fetchall()
    forms.minor.choices = [(row[1], row[1]) for row in minor_data ]
    
    ## gather information from profile_types table and generate a list of profile types.
    cur.execute(""" SELECT * FROM profile_type ORDER BY type ASC """)
    profile_data = cur.fetchall()
    forms.profiletype.choices = [(row[1], row[1]) for row in profile_data ]

    ## if the method is post. then the information will be grabbed from the html and posted into the
    ## database if all the required information is provided
    if request.method == 'POST':
        if forms.validate() == False:
            flash('ALL FIELDS ARE REQURIED')
            return render_template('createprofile.html', forms = forms)
        else:

    ## if all the required information is provided then flask will collect and assign those input fields
    ## to the forms variables and these will be sent into the data table. 
            cur.execute(""" INSERT INTO user(f_name, l_name, email, gender, major, minor,
                            age, user_name, password, phone_number, profile_type, graduate_date,
                            profession, about_me, interests, skills, city, state) VALUES(%s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                        ( forms.firstname.data, forms.lastname.data, forms.email.data, forms.gender.data,
                          forms.major.data, forms.minor.data, forms.age.data, forms.username.data,
                          forms.password.data, forms.phonenumber.data, forms.profiletype.data, forms.graddate.data,
                          forms.profession.data, forms.aboutme.data, forms.interests.data, forms.skills.data, forms.city.data, forms.state.data))

    ## commit changes into the database
            conn.commit
            conn.autocommit(True)

            return redirect(url_for('studentmainpage'))
    elif request.method == 'GET':
        return render_template('createprofile.html', forms = forms)


##  
@application.route('/signinpage', methods=['GET', 'POST'])
def signin():
    ## as extra precaution, the session should be cleared before signing 
    session.clear()

    ## we have encountered situations in which the session did not clear so we
    ## decided to send the user to the home page if that was the case.
    if 'username' in session:
        return redirect(url_for('homepage'))
    error = None
    try:

        ## gather information from the html file and create a variable to be used
        ## when querying the information from the data table
        if request.method == 'POST':
            username_form = request.form['username']
            cur.execute("SELECT COUNT(1) FROM user WHERE user_name = %s", [username_form])
            if not cur.fetchone()[0]:
                ## error if the user name is invalid
                raise ServerError('Invalid username')
            print cur.fetchone()

            ## get the password typed in by the user in the html file and store it into a
            ## variable
            password_form = request.form['password']

            ## get the actual user's password from the table
            cur.execute("SELECT password FROM user WHERE user_name = %s", [username_form])

            ## got through the password (hashing to be implemented)
            for row in cur.fetchall():
                ## if the password collected from the table is the same as the one the user
                ## typed in AND the user in session is the same as the user requesting to
                ## sign in, then allow access and send user to the homepage.
                if password_form == row[0]:
                    session['username'] = request.form['username']

                    return redirect(url_for('homepage'))
            raise ServerError('Invalid password')
    except ServerError as e:
        error = str(e)
    return render_template('signinpage.html')

@application.route('/signout')
def signout():

    ## since we were having issues with clearing sessions, we want to make sure the sessions
    ## are cleared when user signs out.
    session.pop('username', None)
    session.clear()
    session.clear()

    ## call the clearsession function to make sure the session is cleared.
    return redirect(url_for('clearsession'))

@application.route('/clearsession')
def clearsession():

    ## makes sure the session is cleared (one can never be too sure) and redirect to the signin page
    session.clear()
    return redirect('signin')

@application.route('/csharpquestions')
def csharpquestions():

##  Checks login session and assigns variables  
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()
##          forms variable will be used in future iterations.
            return render_template('csharpquestions.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
        return render_template('csharpquestions.html')

@application.route('/experiences')
def experiences():

    ##  Checks login session and assigns variables
    if request.method == 'GET':
        if 'username' in session:
            username=session['username']
            cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
            name =  cur.fetchone()
            cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
            profile = cur.fetchone()
            
##          forms variable will be used in future iterations.
            return render_template('experiences.html', forms=forms, name=name, profile=profile)
        else:
            return redirect(url_for('signin'))
        return render_template('experiences.html')

@application.route('/internships')
def internships():

##  Checks login session and assigns variables
        if request.method == 'GET':
            if 'username' in session:
                username=session['username']
                cur.execute("""SELECT f_name FROM user WHERE user_name = %s""", [username])
                name =  cur.fetchone()
                cur.execute("""SELECT profile_type FROM user WHERE user_name = %s""", [username])
                profile = cur.fetchone()

##          forms variable will be used in future iterations.
                return render_template('internships.html', forms=forms, name=name, profile=profile)
            else:
                return redirect(url_for('signin'))
            return render_template('internships.html')

@application.route('/partfulltime', methods=['POST', 'GET'])
def partfulltime():

    forms =  alumniJobs(request.form)

    ## Post Method seems to be required as the program was breaking since the post was requested
    ## this sessions will be used in the future to 
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
