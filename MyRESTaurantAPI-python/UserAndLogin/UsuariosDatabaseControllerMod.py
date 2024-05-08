import json
import pyodbc
import bcrypt


class UsuariosDatabaseController:

    def __init__(self):

        server = 'DESKTOP-LMJ5G1R\\SQLEXPRESS'  # Nombre del servidor y nombre de instancia (si es necesario)
        database = 'MyRestaurantDataBase'  # Nombre de la base de datos
        username = 'INTEL'  # Nombre de usuario
        password = ''  # Contraseña

        self.conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes;'


    def encrypt_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    def verify_password(self, input_password, hashed_password):
        hashed_password_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password_bytes)
    
    def get_id(self, id_u):
        conn = pyodbc.connect(self.conn_str)
        
        cursor = conn.cursor()
        sql_query = "SELECT * FROM Usuario WHERE id = ?"
    
        cursor.execute(sql_query, id_u)
        user_data = cursor.fetchone() 

        user_dict = {}
        
        if user_data:
            # Estructurar los datos del usuario en un diccionario
            user_dict = {
                'id': user_data[0],
                'contraseña': user_data[1],
                'correo': user_data[2],
                'nombre': user_data[3],
                'apellido': user_data[4],
                'direccion': user_data[5],
                'nivel_acceso': bool(user_data[6])  # Convertir a booleano el valor de nivel_acceso (BIT)
            }

            # Convertir el diccionario a JSON
            #user_json = json.dumps(user_dict, indent=4)
        
        cursor.close()
        conn.close()

        return user_dict
    

    def insert_user(self, pw, email, name, lname, direct, access):
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()

        # Consulta SQL para insertar una nueva reserva
        sql_query = """
            INSERT INTO Usuario (contrasena, correo, nombre, apellido, direccion, nivel_acceso) VALUES
            (?, ?, ?, ?, ?, ?)
        """

        try:
            # Ejecutar la consulta SQL con los parámetros proporcionados
            cursor.execute(sql_query, (self.encrypt_password(pw), email, name, lname, direct, access))
            conn.commit()  # Confirmar la transacción
            print("Reserva insertada exitosamente.")
        except pyodbc.Error as e:
            conn.rollback()  # Revertir la transacción si hay un error
            print(f"Error al insertar la reserva: {e}")

        cursor.close()
        conn.close()
        
        
    def login(self, pw, email):
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()

        # Consulta SQL para actualizar una reserva existente
        sql_query = """
            SELECT id, contrasena from Usuario WHERE correo = ?
        """
        cursor.execute(sql_query, email)
        user_data = cursor.fetchone() 

        user_dict = {
            'id' : 0,
            'correct' : False
            }
        
        if user_data:
            print(pw, user_data[1])
            if self.verify_password(pw, user_data[1]):
                
                user_dict = {
                    'id' : user_data[0],
                    'correct' : True 
                    }
        
        cursor.close()
        conn.close()

        return user_dict

    def update_password(self, id_u, pw):
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()

        # Consulta SQL para actualizar una reserva existente
        sql_query = """
            UPDATE Usuario
            SET contrasena = ?
            WHERE id = ?
        """

        try:
            # Ejecutar la consulta SQL con los parámetros proporcionados
            cursor.execute(sql_query, self.encrypt_password(pw), id_u)
            conn.commit()  # Confirmar la transacción
            print(f"Update con ID {id_u} actualizada exitosamente.")
        except pyodbc.Error as e:
            conn.rollback()  # Revertir la transacción si hay un error
            print(f"Error al actualizar la reserva: {e}")

        cursor.close()
        conn.close()


    
