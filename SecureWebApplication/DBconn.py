import uuid
from SecureWebApplication import db, models, bcrypt


def registerUser(Firstname, Lastname, Email, Password):

    user = models.User(id=str(uuid.uuid4()) ,firstname=Firstname, lastname=Lastname, email=Email, password=Password)
    db.session.add(user)
    db.session.commit()


def getUser(Email, Password):
    user = models.User.query.filter_by(email=Email).first()
    if user and bcrypt.check_password_hash(user.password, Password):
        return user
