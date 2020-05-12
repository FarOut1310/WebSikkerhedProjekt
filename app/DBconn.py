import uuid
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

engine = create_engine('sqlite:////home/kali/Documents/SecureWebAppDB.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    userID = Column(String, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, userID=None, firstName=None, lastName=None, email=None, password=None):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password

def createInitTestData():
    session = Session()
    session.add_all([
        User(str(uuid.uuid4()), 'Bob', 'Lee', 'swagger@email.com', 'swagger1234'),
        User(str(uuid.uuid4()), 'Alice', 'Wunder', 'wunder@email.com', 'Wunderbaum911')
    ])
    session.commit()
    print('users created')

def get_user_with_name_and_password(firstname, password):
    session = Session()
    user = session.query(User).filter(and_(firstname=firstname, password=password))
    return user

def create_user(firstanme, lastname, email, password):
    print('creating user')
    session = Session()
    new_user = User(str(uuid.uuid4()), firstanme, lastname, email, password)
    session.add(new_user)
    session.commit()