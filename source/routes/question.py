from flask import Blueprint, render_template, redirect, request, flash
from utils.database import conexion
from flask_jwt_extended import jwt_required, get_jwt_identity

question= Blueprint('question', __name__)

@question.route('/send_message')
def envio_mensaje():
    return render_template('question/send_message.html')


@question.route('/estudio')
@jwt_required()
def inicio_estudio():
    current_user= get_jwt_identity()
    return render_template('question/estudio.html')   


@question.route('/guardar_encuesta', methods=['GET','POST'])
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
            except Exception as h:
                print(h)
                flash('Debe seleccionar todas las respuestas para poder enviarlas correctamente')
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
            except Exception as h:
                print(h)
                return '<h1> error de conexión</h1>'
        else:
            return render_template('question/estudio.html')
                
   
        
@question.route('/fin_estudio')
def fin_estudio():
    return render_template('question/fin_estudio.html')
