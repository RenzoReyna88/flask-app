from flask import Flask
from flask_mail import Mail
from routes.auth import auth
from routes.question import question
from routes.sitio import sitio
from config import config, USUARIO_GMAIL, PASSWORD_GMAIL, SECRET_KEY_TOKEN
from flask_jwt_extended import JWTManager




app= Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = f'{USUARIO_GMAIL}'
app.config['MAIL_PASSWORD'] = f'{PASSWORD_GMAIL}'
app.config['MAIL_DEFAULT_SENDER'] = f'{USUARIO_GMAIL}'
mail= Mail(app)


app.config['JWT_SECRET_KEY']= F'{SECRET_KEY_TOKEN}'
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
JWT= JWTManager(app) 


app.register_blueprint(auth)
app.register_blueprint(question)
app.register_blueprint(sitio)


def status_401(error):    
    return '<h1>Error 401, no estas autorizado a acceder a esta vista<h1>'

def pagina_no_encontrada(error): 
    return '<h1>Error 404. la pagina que estas buscando no existe</h1>'

                                                              
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(401, status_401)  
    app.run(debug=True, port=9000)
