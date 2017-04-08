from sqlalchemy import Table, Column, Integer, String
from app.database import Base

class User(db.Model):
    query = db_session.query_property()

    def __init__(self, firstname=None, lastname=None, email=None,
        username=None, password=None, city=None, state=None, profileType=None,
        major=None, minor=None, graddate=None, profession=None,
        interests=None, skills=None, aboutme=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password
        self.city = city
        self.state = state
        self.profiletype = profiletype
        self.major = major
        self.minor = minor
        self.graddate = graddate
        self.profession = profession
        self.interests = interests
        self.skills = skills
        self.aboutme = aboutme

    def __repr__(self):
        return '<User %r>' % (self.firstname)

    users = Table('users', metadata,
        id = .Column(Integer, primary_key = True)
        firstname = Column(String(50))
        lastname = Column(String(50))
        email = Column(String(100), unique = True)
        username = Column(String(50), unique = True)
        password = Column(String(100))
        city = Column(String(50))
        state = Column(String(50))
        profiletype = Column(String(10))
        major = Column(String(50))
        minor = Column(String(50))
        graddate = Column(String(50))
        profession = Column(String(100))
        interests = Column(String(100))
        skills = Column(String(100))
        aboutme = Column(String(500)))

        mapper(User, users)
