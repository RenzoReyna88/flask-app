from flask import Blueprint, render_template

proyect= Blueprint('proyect', __name__)


@proyect.route('/propuestas_de_proyectos')
def proyectos():
    return render_template('proyect/propuestas_de_proyectos.html')

@proyect.route('/proyecto_educativo')
def proyecto_educativo():
    return render_template('proyect/proyecto_educativo.html')

@proyect.route('/proyecto_institucion_deportiva')
def proyecto_deportivo():
    return render_template('proyect/proyecto_institucion_deportiva.html')

@proyect.route('/proyecto_municipal')
def proyecto_municipal():
    return render_template('proyect/proyecto_municipal.html')