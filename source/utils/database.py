from config import HOST_DB, USER_DB, PASSWORD_DB, NAME_DB
import mysql.connector

conexion= None

try:
    conexion= mysql.connector.connect(
                                    host= f'{HOST_DB}', 
                                    user= f'{USER_DB}', 
                                    password= f'{PASSWORD_DB}',
                                    db= f'{NAME_DB}',
                                    port= 3306
                                    )    
    if conexion.is_connected:
        print(conexion)
        infoserver= conexion.get_server_info()
        print(infoserver)
except Exception as ex:
        print('Error al realizar la conexión:{}'.format(ex))



