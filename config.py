import os

class Config:
    '''
    Configuration class.
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch'
    SENDER_EMAIL = os.environ.get("MAIL_USERNAME")

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    SECRET_KEY = os.environ.get('SECRET_KEY')

    pass
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}