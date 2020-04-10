import os


DEBUG = True
#要使用session的话就要用这个SECRET_KEY
SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'big_project'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

#跟踪
SQLALCHEMY_TRACK_MODIFICATIONS = False

#用来后台页面session的id， 先随便给一个值、等登陆成功以后
CMS_USER_ID = 'ASDFASDFSA'