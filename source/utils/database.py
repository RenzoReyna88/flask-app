from config import HOST_DB, USER_DB, PASSWORD_DB, NAME_DB
import psycopg2
from psycopg2 import DatabaseError


def connect_to_db():
    try:
        conexion= psycopg2.connect(
                                    host= f'{HOST_DB}', 
                                    user= f'{USER_DB}', 
                                    password= f'{PASSWORD_DB}',
                                    dbname= f'{NAME_DB}',
                                    port= 5432
                                        )    
        if conexion is not None:
            print(conexion)
            return conexion
               
    except DatabaseError as ex:
            print("Error al realizar la conexión:", ex)
            return None
    
        
    
                        

   







