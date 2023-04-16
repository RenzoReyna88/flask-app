from flask import Blueprint
from flask import current_app
from flask import render_template, redirect, request, url_for, flash, render_template_string
from validate_email import validate_email
from utils.database import conexion
import re
from datetime import timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import jwt
from flask_mail import Message, Mail

auth= Blueprint('auth', __name__)

mail= Mail()
@auth.route('/login')
def registro():
    return render_template ('auth/login')


@auth.route('/login')
def login():
  return redirect(url_for('/send_message'))


@auth.route('/auth/login', methods=['GET','POST'])
def login_user():
    from app import mail
    if request.method == 'POST':        
        email= request.form['Username']
        try:
            if validate_email(email):
                patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[c-o-m]{1,3}$'
                if re.match(patron, email):
                    cursor= conexion.cursor()
                    user= email
                    sql_dato="INSERT INTO usuarios_encuestados (email) VALUES ('{0}')".format(user)
                    cursor.execute(sql_dato)
                    conexion.commit()
                    cursor.close()
                    create_token= create_access_token(identity=email,expires_delta=timedelta(hours=1))
                    url_protected = f'http://127.0.0.1:9000/estudio?{create_token}'
                    html = render_template_string('<p>Has click en el siguiente enlace para acceder al estudio: <a href="{{ link }}">{{ link }}</a></p>', link=url_protected)
                    msg= Message(subject='Confirmar correo electrónico', recipients=[email],html=html)
                    msg.body= f'Has click en el siguiente enlace para acceder al estudio:{html}'                    
                    mail.send(msg)
                    print(create_token)                                                                          
                    return redirect('/send_message')
            else:
                flash('Los datos ingresados no son correctos. Verifica la información que has ingresado y vuelve a intentar..')
                return render_template('auth/login.html')
            
        except Exception as ex:
            print(ex)
            flash('Disculpe.. tu ya has participado de este estudio. El programa admite un registro por persona')
            return render_template('auth/login.html')                                                                                                                                                                                                                
    else:
        return render_template('auth/login.html')
    

@auth.route('/auth/base')
def base_login():
    return render_template('auth/base.html')
