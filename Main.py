from flask import Flask
from flask_httpauth import HTTPBasicAuth
import DBConn as DB

app = Flask(__name__)
auth = HTTPBasicAuth()



@auth.get_password
def get_pw(username):
    user = DB.get_user(username)
    if user is not None:
        return username
    return None


@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


if __name__ == '__main__':
    app.run()
