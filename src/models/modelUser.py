from models.entities import User

class ModelUser():
    @classmethod
    def login(self, conexion, email):
        try:
            cursor= conexion.cursor()
            query= "SELECT email FROM usuarios_encuestados WHERE id, email ='{}' ".format(email.email)
            cursor.execute(query)
            fila= cursor.fetchone()
            if fila != None:
                user= User(fila[0], fila[1])
                return user

        except Exception as e:
            raise Exception(e)
        

    @classmethod
    def get_by_id(self, conexion, id):
        try:
            cursor= conexion.cursor()
            query= "SELECT id, email FROM usuarios_encuestados WHERE id = {}".format(id)
            cursor.execute(query)
            fila= cursor.fetchone()
            if fila != None:
                usuario_logeado= User(fila[0], fila[1])
                return usuario_logeado

        except Exception as e:
            raise Exception(e)