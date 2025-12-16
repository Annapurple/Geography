import secrets
from forms.registration_form import RegisterForm
from forms.login_form import LoginForm
from flask import Flask, render_template, redirect, abort, request, url_for, send_file
from flask_login import login_user, LoginManager, logout_user, login_required, current_user
from data import db_session
from data.users import User
from data.tests import Tests

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
    return render_template("text1.html",  test="test1")


@app.route('/text2')
def text2():
    return render_template("text2.html", test="test4")


@app.route('/text3')
def text3():
    return render_template("text3.html",test="test5")


@app.route('/text4')
def text4():
    return render_template("text4.html", test="test6")


@app.route('/text5')
def text5():
    return render_template("text1.html", test="test7")




@app.route('/test1', methods=['GET', 'POST'])
def test1():
    if not current_user.is_authenticated:
        return redirect('/')
    db_sess = db_session.create_session()
    if request.method == 'POST':
        score = 0
        q1 = request.form.getlist('q1')
        if set(q1) == {'1', '6'}:
            score += 1

        if request.form.get('q2') == 'b':
            score += 1

        q3 = set(request.form.getlist('q3'))
        if q3 == {'1', '3', '6'}:
            score += 1

        if request.form.get('q4') == 'b':
            score += 1

        if request.form.get('q5') == 'b':
            score += 1

        if request.form.get('q6') == 'c':
            score += 1

        if request.form.get('q7') == 'a':
            score += 1

        if request.form.get('q8', '').strip().upper() == 'ЕАЭС':
            score += 1

        if request.form.get('q9', '').strip().upper() == 'ВТО':
            score += 1

        if request.form.get('q10', '').strip().upper() == 'ШОС':
            score += 1
        q11_correct = ['Китай', 'Индия', 'США', 'Индонезия', 'Пакистан', 'Нигерия', 'Бразилия', 'Бангладеш', 'Россия']
        q11_raw = request.form.get('q11', '')
        q11_user = [s.strip() for s in q11_raw.split(',')]

        if q11_user == q11_correct:
            score += 1

        if request.form.get('q12') in {'1', '2', '3', '4'}:
            score += 1

        if request.form.get('q13', '').strip() == '16':
            score += 1

        if request.form.get('q14') == 'd':
            score += 1

        if request.form.get('q15') == 'b':
            score += 1

        if request.form.get('q16') == 'b':
            score += 1

        if request.form.get('q17', '').strip() == '9':
            score += 1

        if request.form.get('q18') == 'a':
            score += 1

        if request.form.get('q19') == 'b':
            score += 1

        if request.form.get('q20') == 'b':
            score += 1

        if request.form.get('q21') == 'c':
            score += 1

        if request.form.get('q22') == 'b':
            score += 1

        if request.form.get('q23') == 'b':
            score += 1

        if request.form.get('q24') == 'b':
            score += 1

        if request.form.get('q25') == 'b':
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
    return redirect('/')


@app.route('/test3', methods=['GET', 'POST'])
def test3():
    if not current_user.is_authenticated:
        return redirect('/')
    db_sess = db_session.create_session()
    if request.method == 'POST':
        score = 0

        if request.form.get('q1', '').strip().replace(' ', '') == '3412':
            score += 1

        q2 = set(request.form.getlist('q2'))
        if q2 == {'1', '3', '5'}:
            score += 1

        if request.form.get('q3') == 'b':
            score += 1

        if request.form.get('q4') == 'c':
            score += 1

        if request.form.get('q5') == 'b':
            score += 1

        q6 = set(request.form.getlist('q6'))
        if q6 == {'a', 'c'}:
            score += 1

        q7 = set(request.form.getlist('q7'))
        if q7 == {'a', 'd'}:
            score += 1

        q8 = set(request.form.getlist('q8'))
        if q8 == {'a', 'c'}:
            score += 1

        q9 = set(request.form.getlist('q9'))
        if q9 == {'d'}:
            score += 1

        q10 = set(request.form.getlist('q10'))
        if q10 == {'a', 'c', 'e'}:
            score += 1

        if request.form.get('q11') == 'b':
            score += 1

        if request.form.get('q12') == 'b':
            score += 1

        if request.form.get('q13') == 'C':
            score += 1

        if request.form.get('q14') == 'B':
            score += 1

        if request.form.get('q15') == 'C':
            score += 1

        if request.form.get('q16') == 'A':
            score += 1

        if request.form.get('q17') == 'D':
            score += 1

        if request.form.get('q18') == 'D':
            score += 1

        if request.form.get('q19', '').strip().replace(' ', '').lower() == 'гдвба':
            score += 1

        if request.form.get('q20', '').strip().replace(' ', '') == '4321':
            score += 1

        if request.form.get('q21', '').strip() == '5.7' or request.form.get('q21',
                                                                            '').strip() == '5,7' or request.form.get(
            'q21', '').strip() == '57':
            q21_val = request.form.get('q21', '').strip().replace(',', '.')
            if q21_val == '5.7':
                score += 1

        if request.form.get('q22', '').strip().lower().replace('ё', 'е') in ['эвтрофикация', 'эвтрофикации',
                                                                             'эвтрофикацией']:
            score += 1

        if request.form.get('q23', '').strip().lower() in ['рекультивация', 'рекультивации']:
            score += 1

        q24_ans = request.form.get('q24', '').strip().lower()
        if q24_ans in ['экологической', 'геоэкологической']:
            score += 1

        if request.form.get('q25', '').strip().lower() in ['устойчивым', 'устойчивое']:
            score += 1

        if request.form.get('q26') == 'B':
            score += 1

        q27 = set(request.form.getlist('q27'))
        if q27 == {'A', 'C'}:
            score += 1

        if request.form.get('q28') == 'C':
            score += 1

        if request.form.get('q29') == 'B':
            score += 1

        if request.form.get('q30') == 'D':
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
    return render_template('test4.html')


@app.route('/test4', methods=['GET', 'POST'])
def test4():
    if not current_user.is_authenticated:
        return redirect('/')
    db_sess = db_session.create_session()
    if request.method == 'POST':
        score = 0

        if request.form.get('q1') == 'D':
            score += 1

        if request.form.get('q2') == 'A':
            score += 1

        if request.form.get('q3') == 'B':
            score += 1

        if request.form.get('q4') == 'C':
            score += 1

        if request.form.get('q5') == 'B':
            score += 1

        if request.form.get('q6') == 'B':
            score += 1

        if request.form.get('q7') == 'C':
            score += 1

        if request.form.get('q8') == 'A':
            score += 1

        if request.form.get('q9') == 'C':
            score += 1

        q10 = set(request.form.getlist('q10'))
        if q10 == {'A', 'E'}:
            score += 1

        q11 = set(request.form.getlist('q11'))
        if q11 == {'A', 'E', 'C'}:
            score += 1

        if request.form.get('q12') == 'B':
            score += 1

        if request.form.get('q13', '').strip().replace(' ', '').lower() == 'гбдав':
            score += 1

        q14_correct = "1-Природно-экономические,2-Политические,3-Геополитические,4-Социально-экономические"
        q14_user = request.form.get('q14', '').strip().replace(' ', '')
        if q14_user.lower() == q14_correct.replace(' ', '').lower():
            score += 1

        q15 = set(request.form.getlist('q15'))
        if q15 == {'B', 'D'}:
            score += 1

        if request.form.get('q16') == 'B':
            score += 1

        if request.form.get('q17') == 'B':
            score += 1

        if request.form.get('q18') == 'B':
            score += 1

        if request.form.get('q19') == 'B':
            score += 1

        if request.form.get('q20') == 'B':
            score += 1

        q21 = set(request.form.getlist('q21'))
        if q21 == {'A', 'B'}:
            score += 1

        if request.form.get('q22') == 'C':
            score += 1

        if request.form.get('q23') == 'C':
            score += 1

        if request.form.get('q24') == 'B':
            score += 1

        if request.form.get('q25') == 'B':
            score += 1

        q26 = set(request.form.getlist('q26'))
        if q26 == {'B', 'C'}:
            score += 1

        if request.form.get('q27') == 'B':
            score += 1

        if request.form.get('q28') == 'B':
            score += 1

        if request.form.get('q29') == 'A':
            score += 1

        if request.form.get('q30') == 'D':
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
    return render_template('test4.html')


@app.route('/test5', methods=['GET', 'POST'])
def test5():
    if not current_user.is_authenticated:
        return redirect('/')
    db_sess = db_session.create_session()
    if request.method == 'POST':
        score = 0

        if request.form.get('q1', '').strip().replace(' ', '') == '3412':
            score += 1

        q2 = set(request.form.getlist('q2'))
        if q2 == {'1', '3', '5'}:
            score += 1

        if request.form.get('q3') == 'b':
            score += 1

        if request.form.get('q4') == 'c':
            score += 1

        if request.form.get('q5') == 'b':
            score += 1

        q6 = set(request.form.getlist('q6'))
        if q6 == {'a', 'c'}:
            score += 1

        q7 = set(request.form.getlist('q7'))
        if q7 == {'a', 'd'}:
            score += 1

        q8 = set(request.form.getlist('q8'))
        if q8 == {'a', 'c'}:
            score += 1

        q9 = set(request.form.getlist('q9'))
        if q9 == {'d', "c"}:
            score += 1

        q10 = set(request.form.getlist('q10'))
        if q10 == {'a', 'c', 'e'}:
            score += 1

        if request.form.get('q11') == 'b':
            score += 1

        if request.form.get('q12') == 'b':
            score += 1

        if request.form.get('q13') == 'C':
            score += 1

        if request.form.get('q14') == 'B':
            score += 1

        if request.form.get('q15') == 'C':
            score += 1

        if request.form.get('q16') == 'A':
            score += 1

        if request.form.get('q17') == 'D':
            score += 1

        if request.form.get('q18') == 'D':
            score += 1

        if request.form.get('q19', '').strip().replace(' ', '').lower() == 'гдвба':
            score += 1

        if request.form.get('q20', '').strip().replace(' ', '') == '4321':
            score += 1

        if request.form.get('q21', '').strip() == '5.7' or request.form.get('q21',
                                                                            '').strip() == '5,7' or request.form.get(
            'q21', '').strip() == '57':

            q21_val = request.form.get('q21', '').strip().replace(',', '.')
            if q21_val == '5.7':
                score += 1

        if request.form.get('q22', '').strip().lower().replace('ё', 'е') in ['эвтрофикация', 'эвтрофикации',
                                                                             'эвтрофикацией']:
            score += 1

        if request.form.get('q23', '').strip().lower() in ['рекультивация', 'рекультивации']:
            score += 1

        q24_ans = request.form.get('q24', '').strip().lower()
        if q24_ans in ['экологической', 'геоэкологической']:
            score += 1

        if request.form.get('q25', '').strip().lower() in ['устойчивым', 'устойчивое']:
            score += 1

        if request.form.get('q26') == 'B':
            score += 1

        q27 = set(request.form.getlist('q27'))
        if q27 == {'A', 'C'}:
            score += 1

        if request.form.get('q28') == 'C':
            score += 1

        if request.form.get('q29') == 'B':
            score += 1

        if request.form.get('q30') == 'D':
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
    return render_template('test5.html')


@app.route('/test6', methods=['GET', 'POST'])
def test6():
    if not current_user.is_authenticated:
        return redirect('/')

    db_sess = db_session.create_session()

    if request.method == 'POST':
        score = 0

        if request.form.get('q1') == 'C':
            score += 1

        if request.form.get('q2') == 'B':
            score += 1

        if request.form.get('q3') == 'B':
            score += 1

        if request.form.get('q4') == 'B':
            score += 1

        if request.form.get('q5') == 'B':
            score += 1

        q6_answers = request.form.getlist('q6')
        correct_q6 = {'A', 'C'}
        if set(q6_answers) == correct_q6:
            score += 1

        q7_answers = request.form.getlist('q7')
        correct_q7 = {'A', 'B', 'C'}
        if set(q7_answers) == correct_q7:
            score += 1

        if request.form.get('q8', '').strip().upper() == 'CAB':
            score += 1

        if request.form.get('q9') == 'B':
            score += 1

        if request.form.get('q10') == 'B':
            score += 1

        if request.form.get('q11') == 'B':
            score += 1

        if request.form.get('q12') == 'B':
            score += 1

        if request.form.get('q13') == 'B':
            score += 1

        if request.form.get('q14') == '4':
            score += 1

        if request.form.get('q15') == 'B':
            score += 1

        q16_answers = request.form.getlist('q16')
        correct_q16 = {'A', 'B', 'C'}
        if set(q16_answers) == correct_q16:
            score += 1

        q17_answers = request.form.getlist('q17')
        correct_q17 = {'A', 'B', 'C'}
        if set(q17_answers) == correct_q17:
            score += 1

        if request.form.get('q18', '').strip().upper() == 'ABCCBB':
            score += 1

        if request.form.get('q19') == 'B':
            score += 1

        if request.form.get('q20') == 'B':
            score += 1

        try:
            q21_ans = int(request.form.get('q21', '').strip())
            if q21_ans == 100000:
                score += 1
        except (ValueError, TypeError):
            pass

        if request.form.get('q22') == 'B':
            score += 1

        if request.form.get('q23') == 'B':
            score += 1

        if request.form.get('q24') == 'B':
            score += 1

        if request.form.get('q25') == 'B':
            score += 1

        if request.form.get('q26') == 'A':
            score += 1

        q27_answers = request.form.getlist('q27')
        correct_q27 = {'A', 'B', 'C'}
        if set(q27_answers) == correct_q27:
            score += 1

        if request.form.get('q28') == 'B':
            score += 1

        if request.form.get('q29') == 'C':
            score += 1

        if request.form.get('q30') == 'C':
            score += 1

        if request.form.get('q31') == 'C':
            score += 1

        if request.form.get('q32') == 'C':
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
    return render_template('test6.html')


@app.route('/test7', methods=['GET', 'POST'])
def test7():
    if not current_user.is_authenticated:
        return redirect('/')
    db_sess = db_session.create_session()
    if request.method == 'POST':
        score = 0

        q1 = request.form.get('q1')
        if q1 == 'B':
            score += 1

        q2 = request.form.get('q2')
        if q2 == 'b':
            score += 1

        q3 = request.form.getlist('q3')
        correct_q3 = {'a', 'b', 'd'}
        if set(q3) == correct_q3:
            score += 1

        q4 = request.form.getlist('q4')
        correct_q4 = {'a', 'b', 'd'}
        if set(q4) == correct_q4:
            score += 1

        q5 = request.form.getlist('q5')
        correct_q5 = {'a', 'b'}
        if set(q5) == correct_q5:
            score += 1

        q6 = request.form.get('q6', '').strip().upper()
        if q6 == 'ABCD':
            score += 1

        q7 = request.form.get('q7')
        if q7 == '1':
            score += 1

        q8 = request.form.get('q8', '').strip()
        if q8 == '17':
            score += 1

        q9 = request.form.get('q9')
        if q9 == 'b':
            score += 1

        q10 = request.form.get('q10')
        if q10 == 'b':
            score += 1

        # Вопрос 11
        q11 = request.form.get('q11')
        if q11 == 'd':
            score += 1

        q12 = request.form.get('q12')
        if q12 == 'b':
            score += 1

        q13 = request.form.get('q13')
        if q13 == 'a':
            score += 1

        q14 = request.form.get('q14')
        if q14 == 'd':
            score += 1

        q15 = request.form.get('q15')
        if q15 == 'a':
            score += 1

        q16 = request.form.get('q16')
        if q16 == 'b':
            score += 1

        q17 = request.form.get('q17')
        if q17 == 'b':
            score += 1

        q18 = request.form.get('q18')
        if q18 == 'c':
            score += 1

        q19 = request.form.get('q19')
        if q19 == 'b':
            score += 1

        q20 = request.form.get('q20')
        if q20 == 'a':
            score += 1

        q21 = request.form.get('q21')
        if q21 == 'b':
            score += 1

        q22 = request.form.get('q22')
        if q22 == 'a':
            score += 1

        q23 = request.form.get('q23')
        if q23 == 'b':
            score += 1

        q24 = request.form.get('q24')
        if q24 == 'B':
            score += 1

        q25 = request.form.get('q25')
        if q25 == 'B':
            score += 1

        q26 = request.form.get('q26')
        if q26 == 'd':
            score += 1

        q27 = request.form.get('q27')
        if q27 == 'g':
            score += 1

        q28 = request.form.get('q28')
        if q28 == 'v':
            score += 1

        q29 = request.form.get('q29')
        if q29 == 'g':
            score += 1

        q30 = request.form.get('q30')
        if q30 == 'g':
            score += 1

        q31 = request.form.get('q31')
        if q31 == 'B':
            score += 1

        q32 = request.form.get('q32')
        if q32 == 'b':
            score += 1

        q33 = set(request.form.getlist('q33'))
        if q33 == 'b':
            score += 1

        q34 = set(request.form.getlist('q34'))
        if q34 == "c":
            score += 1

        q35 = set(request.form.getlist('q35'))
        if q35 == 'b':
            score += 1

        q36 = set(request.form.get('q36'))
        if q36 == 'c':
            score += 1

        q37 = request.form.get('q37')
        if q37 == 'b':
            score += 1

        q38 = request.form.get('q38', '').strip()
        if q38 == 'b':
            score += 1

        q39 = request.form.get('q39')
        if q39 == 'b':
            score += 1

        q40 = request.form.get('q40')
        if q40 == 'b':
            score += 1

        q41 = request.form.get('q41')
        if q41 == 'b':
            score += 1

        q42 = request.form.get('q42')
        if q42 == 'a':
            score += 1

        q43 = request.form.get('q43')
        if q43 == 'b':
            score += 1

        q44 = request.form.get('q44')
        if q44 == 'a':
            score += 1

        q45 = request.form.get('q45')
        if q45 == 'b':
            score += 1

        q46 = request.form.get('q46')
        if q46 == 'c':
            score += 1

        q47 = request.form.get('q47')
        if q47 == 'c':
            score += 1

        q48 = request.form.get('q48')
        if q48 == 'c':
            score += 1

        q49 = request.form.get('q49')
        if q49 == 'c':
            score += 1

        q50 = request.form.get('q50')
        if q50 == 'b':
            score += 1

        q51 = request.form.get('q51')
        if q51 == 'b':
            score += 1

        q52 = request.form.get('q52')
        if q52 == 'b':
            score += 1

        q53 = request.form.get('q53')
        if q53 == 'b':
            score += 1

        q54 = request.form.get('q54')
        if q54 == 'b':
            score += 1

        q55 = request.form.get('q55')
        if q55 == 'a':
            score += 1

        q56 = request.form.get('q56')
        if q56 == 'b':
            score += 1

        q57 = request.form.get('q57')
        if q57 == 'b':
            score += 1

        q58 = request.form.get('q58')
        if q58 == 'a':
            score += 1

        q59 = request.form.get('q59')
        if q59 == 'b':
            score += 1

        q60 = request.form.get('q60')
        if q60 == 'c':
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
    return render_template('test7.html')


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
