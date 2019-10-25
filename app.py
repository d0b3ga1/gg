# -*- coding:utf-8 -*-

from flask import Flask, request, redirect, url_for, session
from flask import render_template, flash, jsonify, send_file
from werkzeug import secure_filename
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re, os

app = Flask(__name__)
app.secret_key = 'your secret key'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Thông tin về CSDL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'admin'
# app.config['MYSQL_DB'] = 'crud'
app.config['MYSQL_HOST'] = 'us-cdbr-iron-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'b1df1b284d97c5'
app.config['MYSQL_PASSWORD'] = 'd33a338c'
app.config['MYSQL_DB'] = 'heroku_c4efcd520cec242'


# khởi tạo object chứa thông tin vừa config để kết nối MySQL
mysql = MySQL(app)

'''
    cai dat duong dan
'''
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/static/images'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# /login - đây là trang login, sẽ phục vụ cả GET và POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    # output nếu có gì đó sai...
    msg = ''
    # kiểm tra xem "username" và "password" trong POST requests (req mà user submited) có tồn tại
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # biến cho các thành phần
        username = request.form['username']
        password = request.form['password']
        # kiểm tra xem user đã có trong MySQL chưa
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (
            username, password))
        # lấy 1 kq từ CSDL
        account = cursor.fetchone()
        # Nếu account tồn tại thì đưa vào home 
        if account:
            # lưu trữ thông tin trong session
            # tất nhiên là làm api sẽ tốt hơn nhưng với demo thì thế là dc rồi
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            flash("Xin chào, %s" % account['username'])
            return redirect(url_for('admin'))
        else:
            # nếu acc tồn tại rồi thì gửi thông báo sai identity
            msg = 'Tài khoản không tồn tại hoặc sai mật khẩu!'
    return render_template('login.html', msg=msg)


# /logout - đăng xuất (xóa bỏ các thông tin khỏi session)
@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # redirect về login
   return redirect(url_for('login'))


# /register - đây là trang đăng kí, phục vụ cả GET và POST requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    # output nếu có gì đó sai...
    msg = ''
    # kiểm tra "username", "password" và "email" trong POST requests dã tồn tại chưa
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # các biến cần xét
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # kiểm tra
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', [username])
        account = cursor.fetchone()
        # nếu acc tồn tại thì return msg
        if account:
            msg = 'Tài khoản đã tồn tại!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Địa chỉ email không hợp lệ!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Tên đăng nhập cần chứa ít nhất 1 kí tự số!'
        elif not username or not password or not email:
            msg = 'Chưa điền hết các trường!'
        else:
            # form hợp lệ thì insert vào CSDL
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email))
            mysql.connection.commit()
            msg = 'Đăng kí thành công!'
    elif request.method == 'POST':
        # với trường hợp form rỗng
        msg = 'Chưa điền hết các trường!'
    return render_template('register.html', msg=msg)


# /admin - trang chủ cho người dùng đã đăng kí
# @app.route('/admin')
# def admin():
#     # kiểm tra xem đã đăng nhập
#     if 'loggedin' in session:
#         # nếu đã có thì render home
#         return render_template(
#             'admin.html', username=session['username'])
#     # nếu chưa thì về login page
#     return redirect(url_for('login'))


# /profile - thông tin tài khoản
@app.route('/profile')
def profile():
    # kiểm tra xem đã đăng nhập
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', [session['id']])
        account = cursor.fetchone()
        # render profile
        return render_template(
            'profile.html', account=account)
    # nếu chưa thì về login page
    return redirect(url_for('login'))

@app.route('/admin')
def admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM article")
    data = cur.fetchall()
    cur.close()
    data = data[::-1]

    breaking_news = []
    for i in data:
        if i[1]=='news' and len(breaking_news)<=3:
            breaking_news.append(i)
    
    breaking_events = []
    for i in data:
        if i[1]=='event' and len(breaking_events)<=3:
            breaking_events.append(i)

    return render_template(
        'admin.html', news=breaking_news, events=breaking_events)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM article")
    data = cur.fetchall()
    cur.close()
    data = data[::-1]

    breaking_news = []
    for i in data:
        if i[1]=='news' and len(breaking_news)<=3:
            breaking_news.append(i)
    
    breaking_events = []
    for i in data:
        if i[1]=='event' and len(breaking_events)<=3:
            breaking_events.append(i)

    return render_template(
        'index.html', news=breaking_news, events=breaking_events)

'''
    CRUD api
'''
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Đã thêm bài viết!")
        ctype = request.form['type']
        imgname = request.form['imgname']
        title = request.form['title']
        content = request.form['content']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO article (type, imgname, title, content) VALUES (%s, %s, %s, %s)", (
                ctype, imgname, title, content))
        mysql.connection.commit()
        return redirect(url_for('admin'))


@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Đã xóa bài viết")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM article WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('admin'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        ctype = request.form['type']
        title = request.form['title']
        imgname = request.form['imgname']
        content = request.form['content']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE article
               SET type=%s, imgname=%s, title=%s, content=%s
               WHERE id=%s
            """, (ctype, imgname, title, content, id_data))
        flash("Đã cập nhật bài viết số {id}!".format(id=id_data))
        mysql.connection.commit()
        return redirect(url_for('admin'))

@app.route('/upload',methods=['GET','POST'])
def upload():
    def create_new_folder(local_dir):
        ''' tạo folder trong đường dẫn nếu chưa có
        '''
        newpath = local_dir
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        return newpath

    def allowed_file(filename):
        ''' kiểm tra tệp hợp lệ?
        '''
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    if request.method == "POST":
        file = request.files['image']
        if file and allowed_file(file.filename):
            img = request.files['image']
            img_name = secure_filename(img.filename)
            create_new_folder(app.config['UPLOAD_FOLDER'])
            saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
            img.save(saved_path)
            flash("Đã tải lên: %s" % img_name)
            return render_template('upload.html') 
    return render_template('upload.html')

@app.route('/img/<path:file_name>')
def get_raw(file_name):
    import os.path
    if os.path.exists('{path}/{file}'.format(
        path=UPLOAD_FOLDER, file=file_name)):
        # return 'ok'
        return send_file('{path}/{file}'.format(
            path=UPLOAD_FOLDER, file=file_name), mimetype='image/gif')
    else:
        return "err"



if __name__ == "__main__":
    app.run(debug=True)




