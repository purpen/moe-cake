# -*- coding: utf-8 -*-
"""
    config.py
    ~~~~~~~~~~~~~~~~~

    Default configuration

    :copyright: (c) 2019 by purpen.
"""

import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # change this in your production settings !!!

    MODE = 'dev'

    DOMAIN_URL = 'http://127.0.0.1:9000'

    CSRF_ENABLED = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Moe#2020%0606!'

    # 默认语言, zh_CN,
    BABEL_DEFAULT_LOCALE = 'zh'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    DB_PREFIX = 'moe_'

    # 配置输出SQL语句
    SQLALCHEMY_ECHO = True

    # 每次request自动提交db.session.commit()
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # slow database query threshold (in seconds)
    DATABASE_QUERY_TIMEOUT = 0.5

    # 管理员
    ADMINS = ('purpen.w@gmail.com',)

    # 邮件服务
    DEFAULT_MAIL_SENDER = 'support@qq.com'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'Admin'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'Mic2018'
    MAIL_SUBJECT_PREFIX = '[MIC]'
    MAIL_SENDER = os.environ.get('MAIL_SENDER') or DEFAULT_MAIL_SENDER

    AWS_ACCESS_KEY = 'AKIAJMIYNJXL7QEHTXNQ'
    AWS_ACCESS_SECRET = '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'

    # Can not compress the CSS/JS on Dev environment.
    IMAGE_SIZE = (480, 480)

    # Asset Bucket
    ASSETS_DEBUG = True
    FLASK_ASSETS_USE_CDN = True
    CDN_DEBUG = True
    CDN_HTTPS = True
    CDN_TIMESTAMP = True
    CDN_ENDPOINTS = ['static']
    CDN_DOMAIN = 'kg.erp.taihuoniao.com'
    THUMB_CDN_DOMAIN = 'kg.erp.taihuoniao.com'

    # 七牛存储（生产环境使用云存储）
    QINIU_UPLOAD = 'https://up.qbox.me'
    QINIU_ACCESS_KEY = 'AWTEpwVNmNcVjsIL-vS1hOabJ0NgIfNDzvTbDb4i'
    QINIU_ACCESS_SECRET = 'F_g7diVuv1X4elNctf3o3bNjhEAe5MR3hoCk7bY6'
    QINIU_BUCKET_NAME = 'frking'
    QINIU_CALLBACK_URL = 'https://fx.taihuoniao.com'

    # 日志
    ERROR_LOG = 'logs/moe-error.log'

    # pagination
    MAX_PER_PAGE = 500
    MAX_SEARCH_RESULTS = 50
    POSTS_PER_PAGE = 50

    # css/js
    # BOOTSTRAP_SERVE_LOCAL = False

    UPLOADED_PHOTOS_DEST = basedir + '/public/uploads'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'pem', 'p12'])
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

    # csrf protected
    WTF_CSRF_ENABLED = True

    # Whoose Index of Full Text Search
    WHOOSH_BASE = basedir + '/whooses'

    # Pjax base template
    PJAX_BASE_TEMPLATE = 'pjax.html'

    # Celery Options
    CELERY_IMPORTS = (
        'app.tasks'
    )
    CELERY_BROKER_URL = 'redis://localhost:6379/8'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/9'

    # schedules
    CELERYBEAT_SCHEDULE = {
        'every-minute-demo': {
            'task': 'moe.demo.add_together',
            'schedule': timedelta(seconds=60),
            'args': (1, 1)
        },
        # 每5分钟检测刷新微信token
        # 'wx-refresh-token': {
        #     'task': 'moe.wx.refresh_component_token',
        #     'schedule': timedelta(seconds=300),
        #     'args': ()
        # },
        # 每5分钟检测刷新授权方token
        # 'wx-refresh-authorizer-token': {
        #     'task': 'moe.wx.refresh_authorizer_token',
        #     'schedule': timedelta(seconds=300),
        #     'args': ()
        # },
    }

    # 缓存类型
    # CACHE_REDIS_URL 连接到Redis服务器的URL。
    # 例如：redis://user:password@localhost:6379/2。 仅用于RedisCache。
    CACHE_TYPE = 'redis'
    CACHE_KEY_PREFIX = 'moe_'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = '6379'
    CACHE_REDIS_PASSWORD = ''
    CACHE_REDIS_DB = '2'
    CACHE_REDIS_URL = 'redis://:@localhost:6379/7'

    # Redis 配置
    REDIS_URL = 'redis://:@localhost:6379/7'

    # 大汉短信云
    ACCOUNT = 'dh98732'   # 账号
    # PASSWORD = 'i0fEMS61'  # 密码
    PASSWORD = '14RXk1Ki'
    SIGN = '【乐喜社区】'  # 国内短信签名
    INTL_SIGN = '【LeXi】'  # 国际短信签名
    URL = 'http://www.dh3t.com/json/sms/Submit'

    # es搜索框架
    ELASTICSEARCH_HOST = 'localhost:9200'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    # 七牛存储（生产环境使用云存储）
    QINIU_UPLOAD = 'https://up-z1.qiniup.com'
    QINIU_ACCESS_KEY = 'onRo-YLhNKbhiH1gg6YMPiNzU-LWtr4LZjBEOwOf'
    QINIU_ACCESS_SECRET = 'mcSwe6w2yartkExTYFlhPtJihSq3GEM74tZVX_VG'
    QINIU_BUCKET_NAME = 'beast-s3'
    QINIU_CALLBACK_URL = 'https://open.lexivip.com'

    ASSETS_DEBUG = True
    CDN_DEBUG = True
    CDN_HTTPS = False

    # Examples:
    # mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/moecake'

    # Redis 配置
    REDIS_URL = 'redis://localhost:6379/0'


class TestingConfig(Config):
    MODE = 'test'

    DOMAIN_URL = 'https://www.moecake.com'

    TESTING = True

    # 缓存类型 redis
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = '0'
    CACHE_REDIS_PASSWORD = ''

    # 静态文件
    ASSETS_DEBUG = False
    CDN_DEBUG = False
    CDN_HTTPS = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fxdb@1801?!@127.0.0.1/moeshopy?charset=utf8mb4'

    ERROR_LOG = '/var/log/fxerp/mix-error.log'

    UPLOADED_PHOTOS_DEST = '/data/fxerp/uploads'


class ProductionConfig(Config):
    MODE = 'prod'

    DEBUG_LOG = False
    DEBUG = False

    # 七牛存储（生产环境使用云存储）
    QINIU_UPLOAD = 'https://up-z1.qiniup.com'
    QINIU_ACCESS_KEY = 'onRo-YLhNKbhiH1gg6YMPiNzU-LWtr4LZjBEOwOf'
    QINIU_ACCESS_SECRET = 'mcSwe6w2yartkExTYFlhPtJihSq3GEM74tZVX_VG'
    QINIU_BUCKET_NAME = 'beast-s3'
    QINIU_CALLBACK_URL = 'https://open.moebeast.com'

    # 缓存类型
    # CACHE_REDIS_URL 连接到Redis服务器的URL。
    # 例如：redis://user:password@localhost:6379/2。 仅用于RedisCache。
    CACHE_TYPE = 'redis'
    CACHE_KEY_PREFIX = 'mix_'
    CACHE_REDIS_HOST = '10.16.0.5'
    CACHE_REDIS_PORT = '6379'
    CACHE_REDIS_PASSWORD = 'MixRed0801'
    CACHE_REDIS_DB = '0'

    # Redis 配置，默认KEY
    CACHE_REDIS_URL = 'redis://crs-rd2ftez2:MixRed0801@10.16.0.5:6379/7'
    REDIS_URL = 'redis://crs-rd2ftez2:MixRed0801@10.16.0.5:6379/7'

    # 异步任务
    CELERY_BROKER_URL = 'redis://crs-rd2ftez2:MixRed0801@10.16.0.5:6379/8'
    CELERY_RESULT_BACKEND = 'redis://crs-rd2ftez2:MixRed0801@10.16.0.5:6379/9'

    # 静态文件
    ASSETS_DEBUG = False
    CDN_DEBUG = False
    CDN_HTTPS = True
    CDN_ENDPOINTS = ['static']
    CDN_DOMAIN = 'static.moebeast.com'
    THUMB_CDN_DOMAIN = 's3.lexivip.com'

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Mix@MySQL#1808!@10.16.0.4/moeshopy?charset=utf8mb4'

    ERROR_LOG = '/var/log/moe-core/moe-error.log'

    UPLOADED_PHOTOS_DEST = '/data/uploads'

    # Whoose Index of Full Text Search
    WHOOSH_BASE = '/data/whoose'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

conf_name = os.getenv('FLASK_CONFIG') or 'default'
running_config = config[conf_name]
