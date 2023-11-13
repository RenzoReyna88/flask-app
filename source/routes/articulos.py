from flask import Blueprint, render_template

articulo= Blueprint('articulo', __name__)


@articulo.route('/seguridadcibernetica')
def cyber_seguridad():
    return render_template('articulos/seguridadcibernetica.html')

@articulo.route('/protegetuinfo')
def protyeccion_seguridad():
    return render_template('articulos/protegetuinfo.html')

@articulo.route('/proteccionphone')
def protyeccion_movil():
    return render_template('articulos/proteccionphone.html')