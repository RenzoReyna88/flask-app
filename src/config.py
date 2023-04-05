from dotenv import load_dotenv

import os

load_dotenv()

SECRETKEY= os.environ['secret_key']

# datos para la conexión con la BD
HOST_DB = os.environ['host']
USER_DB = os.environ['user']
PASSWORD_DB = os.environ['password']
NAME_DB = os.environ['db']


#datos gmail   
PASSWORD= os.environ['Password']
SECRET = os.environ['jwt_key']

class DevelopmentConfig():
    SECRET_KEY= os.environ['secret_key']

config={
    'development': DevelopmentConfig
}