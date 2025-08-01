from flask import Blueprint, render_template, redirect, request, flash,jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import jwt

question= Blueprint('question', __name__)

@question.route('/send_message')
def envio_mensaje():    
    return render_template('question/send_message.html')
   

@question.route('/estudio', methods=['GET','POST'])
@jwt_required(locations=['headers','query_string'], optional=False)
def inicio_estudio():
        try:
            email= get_jwt_identity()
            if email: 
                return render_template('question/estudio.html')
            else:
                return jsonify(msg='Token invalido'), 401
       
        except jwt.exceptions.InvalidTokenError:
            response= jsonify(msg='Token inválido')
            response.status_code= 401
            return response
        except Exception as ex:
            print(ex)
            flash('Error de conexión a la base de datos')
            return render_template('auth/login.html')


@question.route('/guardar_encuesta', methods=['POST'])
def guardar_encuesta():
    from utils.database import connect_to_db
    try:
        if request.method == 'POST':
            print("Datos del formulario:", request.form)
            edad = request.form.get('edad')
            profesion = request.form.get('profesion')
            ins = request.form.get('inst')
            sarmiento = request.form.get('residencia')
            trabajo = request.form.get('trabajo')
            comercios = request.form.get('comercios')
            salario = request.form.get('salario')
            ahorro = request.form.get('ahorro')
            coop = request.form.get('coop')
            dispensario = request.form.get('dispensario')
            cim = request.form.get('cim')
            municipalidad = request.form.get('municipalidad')
            muni = request.form.get('muni')
            educar = request.form.get('educar')
            opinion = request.form.get('opinion')

                    
            if not all([edad, profesion, ins, sarmiento, trabajo, comercios, salario, ahorro, coop, dispensario, cim, municipalidad, muni, educar, opinion]):
                raise ValueError('Debe seleccionar todas las respuestas para poder enviarlas correctamente')
                                
            conexion= connect_to_db()
            with conexion.cursor() as cursor:                 
                sentencia = "INSERT INTO respuestas_encuestados (resp_1, resp_2, resp_3, resp_4, resp_5, resp_6, resp_7, resp_8, resp_9, resp_10, resp_11, resp_12, resp_13, resp_14, resp_15) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                valores = (edad, profesion, ins, sarmiento, trabajo, comercios, salario, ahorro, coop, dispensario, cim, municipalidad, muni, educar, opinion)
                cursor.execute(sentencia, valores)
                conexion.commit()
                cursor.close()
            return redirect('/fin_estudio')
        else:
            return render_template('question/estudio.html')

    except ValueError as e:
        print(e)
        flash(str(e))
        return render_template('question/estudio.html')
    except Exception as ex:
        print(ex)
        flash('Error de conexión a la base de datos')
        return render_template('auth/login.html')
        
        
@question.route('/fin_estudio')
def fin_estudio():
    return render_template('question/fin_estudio.html')

@question.route('/historiasarmientina')
def hist_sar():
    return render_template('sarmiento/historiasarmientina.html')

@question.route('/resultados_parciales_del_estudio')
def result_parcial():
    return render_template('sarmiento/resultados_parciales_del_estudio.html')
  