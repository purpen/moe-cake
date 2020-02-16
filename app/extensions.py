# -*- coding: utf-8 -*-

# 国际化和本地化
from flask_babelex import Babel
# 邮件
from flask_mail import Mail
# 数据库连接
from flask_sqlalchemy import SQLAlchemy
# 本地化日期和时间
from flask_moment import Moment
from flask_wtf.csrf import CSRFProtect
from flask_cdn import CDN
# 管理用户认证系统中的认证状态
from flask_login import LoginManager
# 缓存
from flask_caching import Cache
# redis
from flask_redis import FlaskRedis
# 搜索引擎
from flask_elasticsearch import FlaskElasticsearch

db = SQLAlchemy()
csrf = CSRFProtect()
babel = Babel()
cache = Cache()
moment = Moment()
# Flask-Login初始化
login_manager = LoginManager()
# cdn
cdn = CDN()
# redis
redis_store = FlaskRedis()
# search
es = FlaskElasticsearch()
mail = Mail()