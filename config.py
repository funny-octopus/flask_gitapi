import os


class Config(object):
    LOG_PATH = os.environ.get('LOG_PATH') or 'logs'


class TestConfig(Config):
    TESTING = True

