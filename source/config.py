from dotenv import load_dotenv
import os



load_dotenv()

# datos para la conexión con la BD
HOST_DB= os.environ['host']
USER_DB= os.environ['user']
PASSWORD_DB= os.environ['password']
NAME_DB= os.environ['db']


#datos gmail
USUARIO_GMAIL= os.environ['user_gmail']
PASSWORD_GMAIL= os.environ['password_gmail']  

#json web token
SECRET_KEY_TOKEN= os.environ['jwt_key']

class DevelopmentConfig():
    SECRET_KEY= os.environ['secret_key']

config={
    'development': DevelopmentConfig
}