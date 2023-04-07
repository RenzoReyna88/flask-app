from flask import Flask, redirect, render_template, url_for, request, flash, jsonify
from flask_mail import Mail, Message
from utils.database import conexion
import re
from config import config, SECRET, USUARIO_GMAIL ,PASSWORD_GMAIL, SECRETKEY
from utils.database import conexion
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_current_user


app= Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = f'{USUARIO_GMAIL}'
app.config['MAIL_PASSWORD'] = f'{PASSWORD_GMAIL}'
app.config['MAIL_DEFAULT_SENDER'] = f'{USUARIO_GMAIL}'
mail = Mail(app)

app.config['JWT_SECRET_KEY'] = f'{SECRET}'    
jwt = JWTManager(app)


#Urls
@app.route('/')
def inicio():
    return render_template('sitio/index.html')  

@app.route('/educ')
def educar():
    return render_template('sitio/educ.html')

@app.route('/tecno')
def info_tecno():
    return render_template('sitio/tecno.html')

@app.route('/hogar')
def home():
    return render_template('sitio/hogar.html')

@app.route('/guardar_comentarios', methods=['GET', 'POST'])
def guardar_comentarios():
    if request.method == 'POST':
        try:
            usuario= request.form['Name']
            comentario= request.form['Coment']
        except Exception as e:
            flash('Debes completar todos los campos')
            return render_template('sitio/hogar.html')

        try:
            if usuario != "" and comentario !="":
                cursor= conexion.cursor()
                insert= "INSERT INTO comentarios (usuario, comentario) VALUES (%s, %s)"
                valores =(usuario, comentario)
                cursor.execute(insert, valores)
                conexion.commit()
                cursor.close()
                flash('Comentarios enviado con exito')
                return render_template('/hogar') 
        except Exception as e:
            return render_template('sitio/hogar.html')        
    else:
        return render_template('sitio/hogar.html')
    

@app.route('/serv')
def servicios():
    return render_template('sitio/serv.html')    

@app.route('/perfil')
def perfil_admin():
    return render_template('sitio/perfil.html')


# rutas de interacción con el cuestionario

@app.route('/send_message')
def envio_mensaje():  
    return render_template('question/send_message.html')

@app.route('/login')
def registro():
    return render_template ('auth/login')

@app.route('/login')
def login():
  return redirect(url_for('/send_message'))


@app.route('/auth/login', methods=['GET','POST'])
def login_user():
    if request.method == 'POST':        
        _user= request.form['Username'] 
        try:  
            if _user:
                patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if re.match(patron, _user):
                    access_token = create_access_token(identity=_user)
                    #token = access_token.decode('UTF-8')
                    cursor= conexion.cursor()
                    user= _user
                    sql_dato="INSERT INTO usuarios_encuestados (email) VALUES ('{0}')".format(user)
                    cursor.execute(sql_dato)
                    conexion.commit()
                    cursor.close()
                    print(access_token)
                    msg = Message(subject='Confirmación de correo electrónico', recipients=[_user])
                    msg.body = f"Has click aquí para acceder al estudio: {access_token}"
                    mail.send(msg)                    
                    return redirect('/send_message')
            else:
                flash('Error al ingresar los datos. Por favor, verifica los datos ingresados y vuelve a intentarlo..')
                return render_template('auth/login.html')

        except Exception as ex:
            flash('Disculpe.. tu ya has participado de este estudio. El programa admite un registro por persona')
            return render_template('auth/login.html')
                                                                                                                                                                                                                
    else:
        return render_template('auth/login.html')


@app.route('/auth/base')
def base_login():
    return render_template('auth/base.html')

              
@app.route('/estudio')
@jwt_required
def inicio_estudio():
    token = request.args.get('token')
    try:
        payload = jwt.decode(token, SECRETKEY, algorithms=['HS256'])
        email = payload['email']
        return render_template('estudio.html', email=email)
    except jwt.exceptions.InvalidTokenError:
        return 'Token inválido'    
    #return render_template('question/estudio.html')
    
@app.route('/fin_estudio')
def fin_estudio():
    return render_template('question/fin_estudio.html')


@app.route('/guardar_encuesta', methods=['GET','POST'])
def guardar_encuesta():
        if request.method == 'POST':
            try:
                edad= request.form['edad']
                profesion= request.form['profesion']
                ins= request.form['inst']
                sarmiento= request.form['residencia']
                trabajo= request.form['trabajo']
                comercios= request.form['comercios']
                salario= request.form['salario']
                ahorro= request.form['ahorro']
                coop= request.form['coop']
                dispensario= request.form['dispensario']
                cim= request.form['cim']
                municipalidad= request.form['municipalidad']
                muni= request.form['muni']
                educar= request.form['educar']
                opinion= request.form['opinion']
            except Exception as e:
                flash('Debe responder todas la preguntas para poder enviar las respuestas')
                return render_template('question/estudio.html')
            try:
                if edad != '' and profesion != '' and ins != '' and sarmiento != '' and trabajo != '' and comercios != '' and salario != '' and ahorro != '' and coop != '' and dispensario != ''and cim !='' and municipalidad != '' and muni !='' and educar != '' and opinion != '':
                    cursor= conexion.cursor()   
                    sentencia= "INSERT INTO respuestas_encuestados (resp_1, resp_2, resp_3, resp_4, resp_5, resp_6, resp_7, resp_8, resp_9, resp_10, resp_11, resp_12, resp_13, resp_14, resp_15) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    valores = (edad, profesion, ins, sarmiento, trabajo, comercios, salario, ahorro, coop, dispensario, cim, municipalidad, muni, educar, opinion)
                    cursor.execute(sentencia, valores)
                    conexion.commit()
                    cursor.close()
                    return redirect('/fin_estudio')
            except Exception as e:
                return '<h1> error de conexión</h1>'
        else:
            return render_template('question/estudio.html')
    



def status_401(error):    
    return '<h1>Error 401, no estas autorizado a acceder a esta vista<h1>'

def pagina_no_encontrada(error): 
    return '<h1>Error 404. la pagina que estas buscando no existe</h1>'                                                              
    

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(401, status_401) 
   # CSRF.init_app(app)  
    app.run(debug=True, port=9000)
