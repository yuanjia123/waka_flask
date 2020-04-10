from flask import Blueprint


#创建蓝图
#前台页面不需要url_prefix（前缀）
dp = Blueprint("front",__name__)

@dp.route("/")
def index():
    return "前台的主页"