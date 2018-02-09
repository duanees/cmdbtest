#coding=utf-8
import os
#数据库初始化
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = '11q'
PASSWORD = 'jczc@666'
HOST = '172.25.135.121'
PORT = '3306'
DATABASE ='wasu'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,PORT, DATABASE)
SECRET_KEY = os.urandom(24)
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False