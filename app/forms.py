from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField,
    SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class SignupForm(Form):
    firstname = TextField("First Name", [validators.Required("Please enter your name.")])
    lastname = TextField("Last Name", [validators.Required("Please enter your name.")])
    email = TextField("Email", [validators.Required("Please enter your email address.")])
        validators.Email("Please enter your email address.")
    username = TextField("Username", [validators.Required("Please enter a valid username.")])
    password = TextField("Password", [validators.Required("Please enter a password.")])
    city = TextField("City", [validators.Required("Please enter your city.")])
    state = TextField("State", [validators.Required("Please enter your state.")])
    profiletype = SelectField('Profile Type,' choices = [('student', 'Student'), ('alumni', 'Alumni'), ('faculty', 'Faculty')]
    major = SelectField('Major,' choices = [('aaas', 'African and African American Studies'),('amer', 'American Studies'), ('anthro', 'Anthropology'), ('arch', 'Archeology'),
        ('arts', 'Art(Studio)'), ('arth', 'Art History'), ('asia', 'Asian Studies'), ('aus', 'Austrailian Studies'),
        ('biochem', 'Biochemistry/Molecular Biology'), ('bio', 'Biology'), ('busman', 'Business Management'), ('bussoc', 'Business Social Entrepreneurship'),
        ('chem', 'Chemistry'), ('class', 'Classical Studies'), ('com', 'Communication Studies'), ('cms', 'Computer Science'), ('media', 'Critical Media and Cultural Studies'),
        ('cultanthro', 'Cultural Anthropology'), ('dance', 'Dance'), ('econ', 'Economics'), ('edu1', 'Education(Elementary)'), ('edu2', 'Education(Secondary)'),
        ('eng', 'English'), ('envstudies', 'Environmental Studies'), ('film', 'Film Studies'), ('french', 'French'), ('german', 'German'),
        ('globhealth', 'Global Health'), ('healthcare', 'Healthcare Management'), ('his', 'History'), ('hum', 'Humanities'), ('intaff', 'International Affairs'),
        ('intbus', ('International Business'), ('intrel', 'International Relations'), ('jewish', 'Jewish Studies'), ('latincarr', 'Latin American and Carribean Studies'),
        ('marbio', 'Marine Biology'), ('math', 'Mathmatics'), ('mena', 'Middle Eastern and North African Studies'), ('music', 'Music'), ('neuro', 'Neuroscience'),
        ('orgbeh', 'Organizational Behavior'), ('phil', 'Philosophy'), ('phy', 'Physics'), ('pol', 'Political Science'), ('psy', 'Psychology'),
        ('policy', 'Public Policy and Political Economy'), ('rel', 'Religious Studies'), ('rus', 'Russian'), ('soc', 'Sociology'), ('spn', 'Spanish'),
        ('sde', 'Sustainable Development and the Environment'), ('the', 'Theatre Arts'), ('swag', 'Sexuality, Womens and Gender Studies'),
        ('write', 'Writing')]
    minor = SelectField('Minor,' choices = [('aaas', 'African and African American Studies'),('amer', 'American Studies'), ('anthro', 'Anthropology'), ('arch', 'Archeology'),
        ('arts', 'Art(Studio)'), ('arth', 'Art History'), ('asia', 'Asian Studies'), ('aus', 'Austrailian Studies'),
        ('biochem', 'Biochemistry/Molecular Biology'), ('bio', 'Biology'), ('busman', 'Business Management'), ('bussoc', 'Business Social Entrepreneurship'),
        ('chem', 'Chemistry'), ('class', 'Classical Studies'), ('com', 'Communication Studies'), ('cms', 'Computer Science'), ('media', 'Critical Media and Cultural Studies'),
        ('cultanthro', 'Cultural Anthropology'), ('dance', 'Dance'), ('econ', 'Economics'), ('edu1', 'Education(Elementary)'), ('edu2', 'Education(Secondary)'),
        ('eng', 'English'), ('envstudies', 'Environmental Studies'), ('film', 'Film Studies'), ('french', 'French'), ('german', 'German'),
        ('globhealth', 'Global Health'), ('healthcare', 'Healthcare Management'), ('his', 'History'), ('hum', 'Humanities'), ('intaff', 'International Affairs'),
        ('intbus', ('International Business'), ('intrel', 'International Relations'), ('jewish', 'Jewish Studies'), ('latincarr', 'Latin American and Carribean Studies'),
        ('marbio', 'Marine Biology'), ('math', 'Mathmatics'), ('mena', 'Middle Eastern and North African Studies'), ('music', 'Music'), ('neuro', 'Neuroscience'),
        ('orgbeh', 'Organizational Behavior'), ('phil', 'Philosophy'), ('phy', 'Physics'), ('pol', 'Political Science'), ('psy', 'Psychology'),
        ('policy', 'Public Policy and Political Economy'), ('rel', 'Religious Studies'), ('rus', 'Russian'), ('soc', 'Sociology'), ('spn', 'Spanish'),
        ('sde', 'Sustainable Development and the Environment'), ('the', 'Theatre Arts'), ('swag', 'Sexuality, Womens and Gender Studies'),
        ('write', 'Writing')]graddate = TextField("Graduation Date", [validators.Required("Please enter your graduation date, or anticipated date of graduation.")])
    graddate = TextField("Graduation Date", [validators.Required("Please enter your graduation date, or anticipated date of graduation.")])
    profession = TextField("Profession", [validators.Required("Please enter your current occupation.")])
    interests = TextField("What are your professional interets?", [validators.Required("Please enter at least one.")])
    skills = TextField("Skills", [validators.Required("Please enter at least one skill.")])
    aboutme = TextField("Tell us about yourself.", [validators.Required("Please create an about me for your profile.")])

    submit SubmitField("Submit")
