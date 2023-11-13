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

#jwt password
SECRET_JWT= os.environ['jwt_key']

#llave secreta
SECRET_KEY= os.environ['secret_key']