from flask import Blueprint, render_template, request, flash


sitio= Blueprint('sitio', __name__)

@sitio.route('/')
def inicio():
    return render_template('sitio/index.html')  


@sitio.route('/educ')
def educar():
    return render_template('sitio/educ.html')


@sitio.route('/tecno')
def info_tecno():
    return render_template('sitio/tecno.html')

@sitio.route('/hogar')
def home():
    return render_template('sitio/hogar.html')
   

@sitio.route('/guardar_comentarios)', methods=['GET', 'POST'])
def guardar_comentarios():
    from app import get_db_connect
    if request.method == 'POST':
        try:
            usuario= request.form['Name']
            comentario= request.form['Coment']
        except Exception as e:
            print(e)
            return render_template('sitio/hogar.html')
        try:
            if usuario != "" and comentario !="":
                conexion= get_db_connect()
                cursor= conexion.cursor()
                insert= "INSERT INTO comentarios (usuario, comentario) VALUES (%s, %s)"
                valores =(usuario, comentario)
                cursor.execute(insert, valores)
                conexion.commit()
                cursor.close()
                conexion.close()
                flash('Comentarios enviado con exito')
                return render_template('/hogar') 
        except Exception as e:
            print(e)
            flash('Debes completar todos los campos')
            return render_template('sitio/hogar.html')        
    else:
        return render_template('sitio/hogar.html')
    
@sitio.route('/perfil')
def perfil_admin():
    return render_template('sitio/perfil.html')    


@sitio.route('/serv')
def servicios():
    return render_template('sitio/serv.html') 



@sitio.route('/mantenimiento')
def mantenimiento():
    return render_template('sitio/mantenimiento.html')
