from SecureWebApplication import DBconn, app, forms, bcrypt
from flask import redirect, url_for, render_template, flash
from flask_login import login_user


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data, 5).decode('utf-8')
        DBconn.registerUser(form.firstname.data, form.lastname.data, form.email.data, hashed_pw)
        return redirect(url_for('login'))
    return render_template('register.html',  form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    print('test1')
    if form.validate_on_submit():
        print('test2')
        user = DBconn.getUser(form.email.data, form.password.data)
        if user:
            print(user.email, user.firstname)
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful')
    return render_template('login.html',  form=form)


@app.route('/Home', methods=['GET', 'POST'])
def home():
    return render_template('Home.html')


@app.route('/Friend', methods=['GET', 'POST'])
def home():
    return render_template('Home.html')
