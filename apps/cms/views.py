from flask import Blueprint,views,render_template,request,session,redirect,url_for
from .forms import LoginForm
from .models import CMSUser
from .decorator import login_required
import config
#创建蓝图
dp = Blueprint("cms",__name__,url_prefix="/cms")

@dp.route("/")
@login_required
def index():
    return "后台主页"

#类视图

class LoginView(views.MethodView):
    def get(self,message = None):
        return render_template("cms/cms_login.html",message = message)
    def post(self):
        # 生成表单对象
        form = LoginForm(request.form)
        #判断是否验证成功
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remrember.data
            #查询由于 这个邮箱
            user = CMSUser.query.filter_by(email = email).first()
            #如果存在user 并且 和检查密码相等
            if user and user.check_password(password):
                #登录成功以后再去修改config.CMS_USER_ID
                session[config.CMS_USER_ID] = user.id
                if remember:
                    # 设置过期时间是31天
                    session.permanent = True
                #登陆成功、跳到cms.index主页
                return redirect(url_for("cms.index"))
            else:
                print("邮箱或者密码验证错误")
                return self.get(message = "邮箱或者密码验证错误")

        else:
            print(form.errors)
            print("表单验证失败")
            return self.get(message="表单验证失败")


#
dp.add_url_rule("/login/",view_func= LoginView.as_view("login"))
