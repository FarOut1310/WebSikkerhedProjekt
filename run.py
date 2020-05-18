from flask import Flask, request, redirect, url_for, render_template
import flask_login
import backend.DBconn as db

#db.createInitTestData()
app = Flask(__name__)
app.secret_key = 'super secret string'

#login_manager = flask_login.LoginManager()
#login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass


@app.route('/createUser', methods=['GET', 'POST'])
def createUser():
    if request.method == 'GET':
        return render_template('createUser.html')
    if request.method == 'POST':
        print('test 1')
       # if request.form['submit'] == 'Submit_create_user':
        print('test 2')
        db.create_user(request.form['firstname'], request.form['lastname'], request.form['email'], request.form['password'])
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        #if request.form['submit'] == 'submit_login':
        print('prøver at finde en user')
        user = db.get_user_with_name_and_password(request.form['firstname'], request.form['password'])
        print(user.firstname)
        print('fandt ikke nogen user')
        flask_login.login_user(user)
    else:
        return 'Bad Login'
    return redirect(url_for('protected'))

@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


#@login_manager.unauthorized_handler
#def unauthorized_handler():
#    return 'Unauthorized'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)