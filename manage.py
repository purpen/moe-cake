#!venv/bin/python
# -*- coding: utf-8 -*-
import os
from flask_script import Server, Manager, Shell
from flask_script.commands import ShowUrls, Clean
from flask_migrate import Migrate, MigrateCommand
from flask_assets import ManageAssets

from app import create_app, db
from app.assets import assets_env


basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


@manager.command
def test():
    """Run the unit test."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# 常用操作命令
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('show-urls', ShowUrls())
# 清除工作目录中Python编译的.pyc和.pyo文件
manager.add_command('clean', Clean())
# css/js 静态文件压缩
manager.add_command('assets', ManageAssets(assets_env))

# 启动测试服务器
server = Server(host='0.0.0.0', port=9000, use_debugger=True)
manager.add_command('server', server)

if __name__ == '__main__':
    manager.run()
