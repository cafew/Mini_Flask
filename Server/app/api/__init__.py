# coding = utf-8
"""
@author: zhou
@time:2019/12/12 14:56
@File: __init__.py
"""

from flask import Blueprint

api = Blueprint('api', __name__)

from . import views