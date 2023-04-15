from utils.database import conexion
class User(conexion.Model):
    id = conexion.Column(conexion.Integer, primary_key=True)
    email = conexion.Column(conexion.varchar, nullable=False, unique=True)
