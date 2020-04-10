from flask import Blueprint


#创建蓝图
dp = Blueprint("common",__name__,url_prefix="/common/")

@dp.route("/")
def index():
    return "公共的主页"