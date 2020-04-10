from flask import Flask
from exts import db
from apps.cms import dp as cms_dp
from apps.front import dp as front_dp
from apps.common import dp as common_dp
import config


def create_app():
    # 初始化Flask对象  app
    app = Flask(__name__)

    # 配置数据库
    app.config.from_object(config)

    # 前台front   后台 cms   公共的common
    app.register_blueprint(cms_dp)
    app.register_blueprint(front_dp)
    app.register_blueprint(common_dp)

    # 给app初始化配置
    db.init_app(app)

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(port=8000,debug=True)
