import os

from app import app


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'khangdepzai'
