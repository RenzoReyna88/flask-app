from .User import User

class ModelUser():
    def login(self, conexion, user):
        try:
            cursor= conexion.cursor()
            query= "SELECT id, email FROM usuarios_encuestados WHERE email= {}".format(user.email)
            cursor.execute(query)
            fila= cursor.fetchone()
            if fila != None:
                usuario= User(fila[1])
                return usuario
            else:
                None 
        except Exception as ex:
            raise(ex)