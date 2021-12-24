# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - sandhika.yogaswara@gmail.com
"""


import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig():

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'apidata.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "tDQtkqdBMH83nncOGbfh90MADMADtw66"
    JWT_SECRET_KEY = "tDQtkqdBMH83nncOGbfh90MADMADtw66"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
