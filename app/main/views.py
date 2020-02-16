# -*- coding: utf-8 -*-
from flask import g, render_template, request, current_app
from . import main


@main.route('/')
def index():
    return 'Hello, World!'
