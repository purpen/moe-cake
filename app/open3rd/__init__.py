# -*- coding: utf-8 -*-

from flask import Blueprint

open3rd = Blueprint('open3rd', __name__)

from . import views
