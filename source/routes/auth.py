from flask import Blueprint
from flask import render_template, redirect, request, url_for, flash, render_template_string
from validate_email import validate_email
from flask_mail import Message, Mail
from flask_jwt_extended import create_access_token
import requests
from datetime import timedelta

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
    from utils.database import connect_to_db
    from app import mail
    if request.method == 'POST':
        email= request.form['Username']
        ter_y_cond = request.form.get('acepta_terminos') == 'on'

        if not validate_email(email):
            flash('Los datos ingresados no son correctos. Verifica la información que has ingresado y vuelve a intentar..')
            return redirect('login')
        elif not ter_y_cond:
            flash('Acepta los términos y condiciones para poder participar')
            return redirect('login')

        try:
            conexion= connect_to_db()
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios_encuestados WHERE email=%s", (email,))
                
                if cursor.fetchone():
                    flash('Disculpe.. usted ya ha participado de este estudio. El programa admite un registro por persona')
                    return redirect('login')
                
                user= email
                insert_data= "INSERT INTO usuarios_encuestados (email,acepta_terminos ) VALUES(%s,%s)"
                cursor.execute(insert_data, (user, ter_y_cond))
                conexion.commit()
                cursor.close()
                create_token= create_access_token(identity=email, expires_delta=timedelta(minutes=30))
                url_protected= 'http://www.desarrolladorsarmientino.com/estudio?jwt={}'.format(create_token)
                headers = {
                            "Authorization": f"Bearer {create_token}"
                            }
                response = requests.get(url_protected, headers=headers)
                html = render_template_string('<p>Has click en el siguiente enlace para acceder al estudio: <a href="{{ link }}">{{ link }}</a></p>', link=url_protected)
                msg= Message(subject='Confirmar correo electrónico', recipients=[email],html=html)
                msg.body= f'Has click en el siguiente enlace para acceder al estudio:{html}'
                mail.send(msg)
            return redirect('/send_message')
        
        except ValueError as ex:
            flash(str(ex))
            return render_template('auth/login.html')
        except Exception as ex:
            print(ex)
            flash('Error de conexión...')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
    

@auth.route('/auth/base')
def base_login():
    return render_template('auth/base.html')


