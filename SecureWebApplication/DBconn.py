import base64
import datetime
import uuid
import io
import os
import secrets
from SecureWebApplication import db, models, bcrypt, app


def registerUser(Firstname, Lastname, Email, Password):

    user = models.User(id=str(uuid.uuid4()) ,firstname=Firstname, lastname=Lastname, email=Email, password=Password)
    db.session.add(user)
    db.session.commit()


def getUser(Email, Password):
    user = models.User.query.filter_by(email=Email).first()
    if user and bcrypt.check_password_hash(user.password, Password):
        return user


def addFriend(Id, Email):
    to_be_friend = models.User.query.filter_by(email=Email).first()
    friend = models.Friends(id=str(uuid.uuid4()), user_id=Id, friend_id=to_be_friend.id)
    print(friend)
    db.session.add(friend)
    db.session.commit()

def getPictures(user_id):
    friendlist = models.Friends.query.filter(models.Friends.user_id == user_id).all()
    image_list = []
    for friend in friendlist:
        list = models.Image.query.filter_by(user_id=friend.friend_id).all()
        for image in list:
            image_list.append(image.image_name)
        print(image_list)
    return image_list

def uploadImage(imagedata, user_id):
    #filesystem setup
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(imagedata.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/pictures', picture_filename)
    imagedata.save(picture_path)
    timestamp = datetime.datetime.today()
    image = models.Image(id=str(uuid.uuid4()), user_id=user_id, image_data=picture_path, image_name=picture_filename, upload_date=timestamp)
    print(image)
    db.session.add(image)
    db.session.commit()

    ##Database setup
    #print(imagedata, imagename, user_id)
    #binaryImageData = io.BytesIO(base64.b64encode(imagedata))
    #timestamp = datetime.datetime()
    #image = models.Image(id=str(uuid.uuid4()), user_id=user_id, image_data=binaryImageData, image_name=imagename, upload_date=timestamp)
    #print(imagedata, imagename, user_id)
    #db.session.add(image)