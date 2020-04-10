#encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from waka_flask import create_app
from exts import db
#把蓝图 cms下面的所有模型都导过来
from apps.cms import models as cms_models

#导入CMSUser  后台操作数据表
CMSUser = cms_models.CMSUser

app = create_app()

#命令行flask_script 下面的Manager
manager = Manager(app)
# 使用Migrate绑定app和db
migrate = Migrate(app,db)
# 添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)

#通过manage.py这样一个程序、后台管理程序cms添加用户
@manager.option("-u","--username",dest="username")
@manager.option("-p","--password",dest="password")
@manager.option("-e","--email",dest="email")
def create_cms_user(username,password,email):
    user = CMSUser(username = username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print("cms用户添加程序")

# cmd 执行 python manage.py create_cms_user -u wakaak -p 123456 -e 110@qq.com
# python manage.py create_cms_user -u zhiliao -p 111111 -e 871105356@qq.com
# 就会增加两条数据

if __name__ == "__main__":
    manager.run()

'''
cmd  去操作这三句话
python manage.py db init

如果已经存在一张表，继续增加表，只需要1、from models import（表明） 2、执行下面语句 
python manage.py db migrate
python manage.py db upgrade
'''