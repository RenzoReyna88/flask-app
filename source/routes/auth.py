from flask import Blueprint
from flask import render_template, redirect, request, url_for, flash, render_template_string
from validate_email import validate_email
import re
from flask_mail import Message, Mail
from flask_jwt_extended import create_access_token
import requests
from datetime import datetime, timedelta

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
    from utils.database import conexion
    from app import mail 
    if request.method == 'POST':        
        email= request.form['Username']
        try:
            if validate_email(email):
                patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[.][(a-z)]{2,4}$'
                if re.match(patron, email):
                    cursor= conexion.cursor()
                    user= email
                    insert_data= "INSERT INTO usuarios_encuestados (email) VALUES('{0}')".format(user)
                    cursor.execute(insert_data)
                    conexion.commit()
                    cursor.close()
                    create_token= create_access_token(identity=email, expires_delta=timedelta(minutes=30))
                    url_protected= 'http://127.0.0.1:9000/estudio?jwt={}'.format(create_token)                    
                    headers = {
                        "Authorization": f"Bearer {create_token}"
                    }
                    response = requests.get(url_protected, headers=headers)
                    html = render_template_string('<p>Has click en el siguiente enlace para acceder al estudio: <a href="{{ link }}">{{ link }}</a></p>', link=url_protected)
                    msg= Message(subject='Confirmar correo electrónico', recipients=[email],html=html)
                    msg.body= f'Has click en el siguiente enlace para acceder al estudio:{html}'                    
                    mail.send(msg) 
                    print(create_token)
                    print(response.content)                                                                     
                    return redirect('/send_message')
            else:
                flash('Los datos ingresados no son correctos. Verifica la información que has ingresado y vuelve a intentar..')
                return render_template('auth/login.html')
            
        except Exception as ex:
            print(ex)
            flash('Disculpe.. usted ya ha participado de este estudio. El programa admite un registro por persona')
            return render_template('auth/login.html')                                                                                                                                                                                                                
    else:
        return render_template('auth/login.html')
    

@auth.route('/auth/base')
def base_login():
    return render_template('auth/base.html')


