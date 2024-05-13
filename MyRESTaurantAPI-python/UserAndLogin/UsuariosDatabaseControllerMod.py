import json
import pymysql
import os
import bcrypt

class UsuariosDatabaseController:

    def __init__(self):

        self.conn = pymysql.connect(unix_socket='/cloudsql/proyectosoa-422123:us-central1:test-mysql',
                                user='root',
                                password=os.environ["DB_PASS"],
                                database='MyRestaurantDataBase',
                                cursorclass=pymysql.cursors.DictCursor)

    def encrypt_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    def verify_password(self, input_password, hashed_password):
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))

    def get_id(self, id_u):
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    sql_query = "SELECT * FROM Usuario WHERE id = %s"
                    cursor.execute(sql_query, (id_u,))
                    user_data = cursor.fetchone()

                    if user_data:
                        user_dict = {
                            'id': user_data['id'],
                            'contraseña': user_data['contrasena'],
                            'correo': user_data['correo'],
                            'nombre': user_data['nombre'],
                            'apellido': user_data['apellido'],
                            'direccion': user_data['direccion'],
                            'nivel_acceso': bool(user_data['nivel_acceso'])  # Convertir a booleano el valor de nivel_acceso (BIT)
                        }
                        return user_dict
                    else:
                        return {}
        except Exception as e:
            print(f"Error: {e}")
            return {}

    def insert_user(self, pw, email, name, lname, direct, access):
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    sql_query = """
                        INSERT INTO Usuario (contrasena, correo, nombre, apellido, direccion, nivel_acceso) VALUES
                        (%s, %s, %s, %s, %s, %s)
                    """
                    encrypted_pw = self.encrypt_password(pw)
                    cursor.execute(sql_query, (encrypted_pw, email, name, lname, direct, access))
                    self.conn.commit()
                    print("Usuario insertado exitosamente.")
        except Exception as e:
            print(f"Error: {e}")
            return {}

    def login(self, pw, email):
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    sql_query = "SELECT id, contrasena FROM Usuario WHERE correo = %s"
                    cursor.execute(sql_query, (email,))
                    user_data = cursor.fetchone()

                    if user_data and self.verify_password(pw, user_data['contrasena']):
                        return {'id': user_data['id'], 'correct': True}
                    else:
                        return {'id': 0, 'correct': False}
        except Exception as e:
            print(f"Error: {e}")
            return {}

    def update_password(self, id_u, pw):
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    sql_query = "UPDATE Usuario SET contrasena = %s WHERE correo = %s"
                    encrypted_pw = self.encrypt_password(pw)
                    cursor.execute(sql_query, (encrypted_pw, id_u))
                    self.conn.commit()
                    print(f"Contraseña actualizada para el usuario con ID {id_u}.")
        except Exception as e:
            print(f"Error: {e}")
            return {}
