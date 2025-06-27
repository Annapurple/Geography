import secrets
import requests
from datetime import datetime
from forms.registration_form import RegisterForm
from forms.login_form import LoginForm
from flask import Flask, render_template, redirect, abort, request, url_for, send_file
from flask_login import login_user, LoginManager, logout_user, login_required, current_user
from data import db_session
from data.users import User
from data.tests import Tests
from data.test1 import Test1

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
db_session.global_init("db/geography.db")
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def page():
    return render_template("main_page.html")


@app.route('/text1')
def text1():
    ls = []
    with open("text1.txt", 'r') as file:
        for line in file:
            ls.append(line.strip())
    return render_template("texts.html", ls=ls, test="test1")


@app.route('/text2')
def text2():
    ls = []
    with open("text2.txt", 'r') as file:
        for line in file:
            ls.append(line.strip())
    return render_template("texts.html", ls=ls, test="test2")


@app.route('/text3')
def text3():
    ls = []
    with open("text3.txt", 'r') as file:
        for line in file:
            ls.append(line.strip())
    return render_template("texts.html", ls=ls, test="test3")


@app.route('/text4')
def text4():
    ls = []
    with open("text4.txt", 'r') as file:
        for line in file:
            ls.append(line.strip())
    return render_template("texts.html", ls=ls, test="test4")


@app.route('/text5')
def text5():
    ls = []
    with open("text5.txt", 'r') as file:
        for line in file:
            ls.append(line.strip())
    return render_template("texts.html", ls=ls, test="test5")


@app.route('/text6')
def text6():
    ls = []
    with open("text6.txt", 'r') as file:
        for line in file:
            ls.append(line.strip())
    return render_template("texts.html", ls=ls, test="test6")


@app.route('/text7')
def text7():
    ls = []
    with open("text7.txt", 'r') as file:
        for line in file:
            ls.append(line.strip())
    return render_template("texts.html", ls=ls, test="test7")


@app.route('/text8')
def text8():
    ls = []
    with open("text8.txt", 'r') as file:
        for line in file:
            ls.append(line.strip())
    return render_template("texts.html", ls=ls, test="test8")


@app.route('/test1', methods=['GET', 'POST'])
def test1():
    db_sess = db_session.create_session()
    if request.method == 'POST':
        age_answer = request.form.get('age')
        name_answer = request.form.get('name')
        score = 0
        if age_answer == '18':
            score += 1
        if name_answer == 'Анна':
            score += 1
        user_id = current_user.id
        test_entry = db_sess.query(Tests).filter(Tests.user_id == user_id).first()
        if test_entry:
            test_entry.test1 = score
        else:
            test_entry = Tests(user_id=user_id, test1=score)
            db_sess.add(test_entry)
        db_sess.commit()
        return redirect('/')
    return render_template('test1.html')


@app.route('/test2', methods=['GET', 'POST'])
def test2():
    db_sess = db_session.create_session()
    if request.method == 'POST':
        age_answer = request.form.get('age')
        name_answer = request.form.get('name')
        score = 0
        if age_answer == '18':
            score += 1
        if name_answer == 'Анна':
            score += 1
        user_id = current_user.id
        test_entry = db_sess.query(Tests).filter(Tests.user_id == user_id).first()
        if test_entry:
            test_entry.test2 = score
        else:
            test_entry = Tests(user_id=user_id, test2=score)
            db_sess.add(test_entry)
        db_sess.commit()
        return redirect('/')
    return render_template('test1.html')


@app.route('/test3', methods=['GET', 'POST'])
def test3():
    db_sess = db_session.create_session()
    if request.method == 'POST':
        age_answer = request.form.get('age')
        name_answer = request.form.get('name')
        score = 0
        if age_answer == '18':
            score += 1
        if name_answer == 'Анна':
            score += 1
        user_id = current_user.id
        test_entry = db_sess.query(Tests).filter(Tests.user_id == user_id).first()
        if test_entry:
            test_entry.test3 = score
        else:
            test_entry = Tests(user_id=user_id, test3=score)
            db_sess.add(test_entry)
        db_sess.commit()
        return redirect('/')
    return render_template('test1.html')


@app.route('/test4', methods=['GET', 'POST'])
def test4():
    db_sess = db_session.create_session()
    if request.method == 'POST':
        age_answer = request.form.get('age')
        name_answer = request.form.get('name')
        score = 0
        if age_answer == '18':
            score += 1
        if name_answer == 'Анна':
            score += 1
        user_id = current_user.id
        test_entry = db_sess.query(Tests).filter(Tests.user_id == user_id).first()
        if test_entry:
            test_entry.test4 = score
        else:
            test_entry = Tests(user_id=user_id, test4=score)
            db_sess.add(test_entry)
        db_sess.commit()
        return redirect('/')
    return render_template('test1.html')


@app.route('/test5', methods=['GET', 'POST'])
def test5():
    db_sess = db_session.create_session()
    if request.method == 'POST':
        age_answer = request.form.get('age')
        name_answer = request.form.get('name')
        score = 0
        if age_answer == '18':
            score += 1
        if name_answer == 'Анна':
            score += 1
        user_id = current_user.id
        test_entry = db_sess.query(Tests).filter(Tests.user_id == user_id).first()
        if test_entry:
            test_entry.test5 = score
        else:
            test_entry = Tests(user_id=user_id, test5=score)
            db_sess.add(test_entry)
        db_sess.commit()
        return redirect('/')
    return render_template('test1.html')


@app.route('/test6', methods=['GET', 'POST'])
def test6():
    db_sess = db_session.create_session()
    if request.method == 'POST':
        age_answer = request.form.get('age')
        name_answer = request.form.get('name')
        score = 0
        if age_answer == '18':
            score += 1
        if name_answer == 'Анна':
            score += 1
        user_id = current_user.id
        test_entry = db_sess.query(Tests).filter(Tests.user_id == user_id).first()
        if test_entry:
            test_entry.test6 = score
        else:
            test_entry = Tests(user_id=user_id, test6=score)
            db_sess.add(test_entry)
        db_sess.commit()
        return redirect('/')
    return render_template('test1.html')


@app.route('/test7', methods=['GET', 'POST'])
def test7():
    db_sess = db_session.create_session()
    if request.method == 'POST':
        age_answer = request.form.get('age')
        name_answer = request.form.get('name')
        score = 0
        if age_answer == '18':
            score += 1
        if name_answer == 'Анна':
            score += 1
        user_id = current_user.id
        test_entry = db_sess.query(Tests).filter(Tests.user_id == user_id).first()
        if test_entry:
            test_entry.test7 = score
        else:
            test_entry = Tests(user_id=user_id, test7=score)
            db_sess.add(test_entry)
        db_sess.commit()
        return redirect('/')
    return render_template('test1.html')


@app.route('/test8', methods=['GET', 'POST'])
def test8():
    db_sess = db_session.create_session()
    if request.method == 'POST':
        age_answer = request.form.get('age')
        name_answer = request.form.get('name')
        score = 0
        if age_answer == '18':
            score += 1
        if name_answer == 'Анна':
            score += 1
        user_id = current_user.id
        test_entry = db_sess.query(Tests).filter(Tests.user_id == user_id).first()
        if test_entry:
            test_entry.test8 = score
        else:
            test_entry = Tests(user_id=user_id, test8=score)
            db_sess.add(test_entry)
        db_sess.commit()
        return redirect('/')
    return render_template('test1.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    db_sess = db_session.create_session()
    tests = db_sess.query(Tests).all()
    new_test = []
    class_filter = request.args.get('class_filter', '')
    users = db_sess.query(User).filter(User.id != 1).order_by(User.class_choice, User.surname).all()
    for test in tests:
        t = test.to_dict(only=["id", "user_id", "test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8"])
        user = next((u for u in users if u.id == t["user_id"]), None)
        if user:
            t["user_id"] = f"{user.name} {user.surname}"
            t["id"] = user.id
            t["class_choice"] = user.class_choice
            if test.test1:
                t["test1"] = test.test1
            else:
                t["test1"] = 0
            if test.test2:
                t["test2"] = test.test2
            else:
                t["test2"] = 0
            if test.test3:
                t["test3"] = test.test3
            else:
                t["test3"] = 0
            if test.test4:
                t["test4"] = test.test4
            else:
                t["test4"] = 0
            if test.test5:
                t["test5"] = test.test5
            else:
                t["test5"] = 0
            if test.test6:
                t["test6"] = test.test6
            else:
                t["test6"] = 0
            if test.test7:
                t["test7"] = test.test7
            else:
                t["test7"] = 0
            if test.test8:
                t["test1"] = test.test8
            else:
                t["test8"] = 0
            if class_filter == '' or t["class_choice"] == class_filter:
                new_test.append(t)
    return render_template("results_page.html", test=new_test)


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
            class_choice=form.class_choice.data
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
