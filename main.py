import secrets
import requests
from datetime import datetime
from forms.registration_form import RegisterForm
from forms.login_form import LoginForm
from flask import Flask, render_template, redirect, abort, request, url_for, send_file
from flask_login import login_user, LoginManager, logout_user, login_required, current_user
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
db_session.global_init("db/travelers.db")
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def text():
    db_sess = db_session.create_session()
    return render_template("base.html")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect('/')
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Register form',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Register form',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Register form', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect('/')
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Authorization', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.errorhandler(401)
def unauthorized(e):
    return render_template('401.html'), 401


@app.errorhandler(403)
def unauthorized(e):
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
