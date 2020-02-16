# -*- coding: utf-8 -*-
"""
    __init__.py
    ~~~~~~~~~~~~~~
    :copyright: (c) 2019 by purpen.
"""
import os
from flask import Flask
# 导入扩展
from .extensions import (
    db,
    mail,
    csrf,
    babel,
    cache,
    cdn,
    moment,
    login_manager,
    redis_store,
    es
)
from .assets import assets_env, bundles
# 导入配置参数
from config import config

# 属性可以设为None、'basic' 或'strong'
login_manager.session_protection = 'strong'

# 设置登录页面的端点
login_manager.login_view = 'auth.login'
login_manager.login_message = '请先登录'
login_manager.login_message_category = 'danger'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)
    babel.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    assets_env.init_app(app)
    assets_env.register(bundles)
    # cdn
    cdn.init_app(app)

    # 缓存
    cache.init_app(app)
    # redis
    redis_store.init_app(app)

    # search
    es.init_app(app)

    # attach routes

    from .adminlte import adminlte as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/adminlte')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/v1.0')

    from .open3rd import open3rd as open_blueprint
    app.register_blueprint(open_blueprint, url_prefix='/open')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
