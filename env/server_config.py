# config file for flask reverse proxy

class Config(object):
    HOST = "0.0.0.0"
    PORT = 8080
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 3000

class TestingConfig(Config):
    TESTING = True