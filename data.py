from mysql.connector import connect, Error, errorcode
from decouple import config


class DataBase:
    def __init__(self):
        self.conexion = {
            'user': config('MYSQL_USER'),
            'password': config('MYSQL_PASSWORD'),
            'host': config('MYSQL_HOST'),
            'database': config('MYSQL_DB'),
            'port': config('MYSQL_PORT')
        }

    def comando(self, consulta):

        try:
            with connect(**self.conexion) as conexion:
                with conexion.cursor(buffered=True) as cursor:
                    cursor.execute(consulta)

                    if consulta.upper().startswith('SELECT'):
                        data = cursor.fetchall()
                    else:
                        conexion.commit()
                        data = cursor.fetchall()
                return data
        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Algo salió mal con el nombre de usuario o la contraseña')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('La base de datos no existe')
            else:
                print(err)
