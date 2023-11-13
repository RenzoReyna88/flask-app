from flask import Flask, jsonify
from flask_mail import Mail
from config import USUARIO_GMAIL, PASSWORD_GMAIL, SECRET_JWT, SECRET_KEY
from flask_jwt_extended import JWTManager
from routes.auth import auth
from routes.question import question
from routes.sitio import sitio
from routes.articulos import articulo



app= Flask(__name__)


app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USE_SSL']= True
app.config['MAIL_USERNAME']= f'{USUARIO_GMAIL}'
app.config['MAIL_PASSWORD']= f'{PASSWORD_GMAIL}'
app.config['MAIL_DEFAULT_SENDER']= f'{USUARIO_GMAIL}'
mail= Mail(app)

app.config['SECRET_KEY']= f'{SECRET_KEY}'

app.config['JWT_SECRET_KEY']= f'{SECRET_JWT}'
JWT= JWTManager(app)

app.register_blueprint(auth)
app.register_blueprint(question)
app.register_blueprint(sitio)
app.register_blueprint(articulo)


def status_401(error):   
    return '<h1>Error 401. No está autorizado a acceder esta vista</h1>'

def pagina_no_encontrada(error): 
   return jsonify(msg='Token inválido'), 401

                                                              
if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(401, status_401)  
    app.run(debug=True)
