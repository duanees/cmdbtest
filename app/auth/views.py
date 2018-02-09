#coding=utf-8
from flask import render_template,request,redirect,url_for,session,g
from app.auth import auth
from app.models import User
from app import db
from app.auth.forms import LoginForm,RegistForm
from flask_login import logout_user,login_required
from app import util

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("auth/newlogin.html",form=form)
    else:
        username = form.name.data
        password = form.password.data
        user = util.login(username,password)
        if user :
            session['user_id'] = user.dgdh
            return redirect(url_for("main.index"))
        else:
            return "账号密码错误"

@auth.route('/regist',methods =['GET','POST'])
def regist():
    form = RegistForm()
    if request.method == "GET":
        return render_template('auth/regist.html',form=form)
    else:
        username = form.name.data
        worknum = form.worknum.data
        password1 = form.password1.data
        password2 = form.password2.data
        work = util.get_worknum(worknum)
        if work:
            return "此工号已经被注册，请更换"
        else:
            if password1 != password2:
                return "两次密码输入不同，请重新输入"
            else:
                util.add_regiest(worknum,username,password1)
                return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
