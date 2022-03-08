import os

class Config:
    '''
    Configuration class.
    '''
    # SECRET_KEY = "906gbg5c64346xrs43535x46u9h687b8767"
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Vanilla@localhost/pitchMain'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False    
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
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Vanilla@localhost/pitchMain'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Vanilla@localhost/pitchMain'

    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}