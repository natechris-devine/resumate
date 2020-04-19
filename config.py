# configuartion for application
import os

DRIVER = "postgresql"

class Config():
    """ Base configuration """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def create_uri():
        """ create database uri based on config from .env file """
        username = os.environ.get('USERNAME')
        password = os.environ.get('PASSWORD')
        ip = os.environ.get('IP')
        port = os.environ.get('PORT')
        port = f":{port}" if port else ""
        dbname = os.environ.get('DBNAME')

        if not username:
            return os.environ.get('SQLALCHEMY_DATABASE_URI')

        return f"{DRIVER}://{username}:{password}@{ip}{port}/{dbname}"


class DevConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = Config.create_uri()
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgresr:postgresr@localhost/resumate_knowledge'

    


class ProdConfig(Config):
    pass


