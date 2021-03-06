#!/usr/bin/python
# -*-coding:utf-8-*-

""" 
Init Flerken App
"""

__author__ = 'Yao Zhang & Zhiyang Zeng'
__copyright__   = "Copyright 2019, Apache License 2.0"

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .config.global_config import APP_CONFIG

app = Flask(__name__)
CSRFProtect(app)

app.debug = APP_CONFIG['DEBUG']
app.secret_key = APP_CONFIG['SECRET_KEY']
if APP_CONFIG['QPS_LIMIT'] == True:
    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=APP_CONFIG['LIMIT_SETTING'],
    )

import flerken.landing
import flerken.detection
