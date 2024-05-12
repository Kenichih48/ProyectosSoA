import json
import pyodbc

class ReservationDatabaseController:

    def __init__(self):

        server = 'DESKTOP-LMJ5G1R\\SQLEXPRESS'  # Nombre del servidor y nombre de instancia (si es necesario)
        database = 'MyRestaurantDataBase'  # Nombre de la base de datos
        username = 'INTEL'  # Nombre de usuario
        password = ''  # Contraseña

        self.conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes;'

        
    def get_state(self, is_free):
        return "Free" if not is_free else "Booked"

    def set_state(self, state):
        if (state == "Free"):
            return False
        else:
            return True
    
    def get_current_state(self):
        conn = pyodbc.connect(self.conn_str)
        
        cursor = conn.cursor()
        sql_query = "SELECT * FROM Reservaciones"
    
        cursor.execute(sql_query)
        reservations = cursor.fetchall()

        #print(reservations)
        result = []

        # Procesar cada tupla de datos y convertir en formato JSON
        for item in reservations:
            id_str, time_str, date_str, is_free, people_quant, id_user = item
            time_formatted = time_str.split('.')[0]  # Obtener solo la hora sin microsegundos
            state = self.get_state(is_free)
            
            # Construir el objeto JSON para cada elemento
            json_obj = {
                "Id" : id_str,
                "Date": date_str,
                "Time": time_formatted,
                "State": state,
                "people_quant": people_quant,
                "id_user": id_user
            }
            result.append(json_obj)
            
            # Agregar el objeto JSON al resultado
        #print(result)
        cursor.close()
        conn.close()

        return result
    

    def insert_reservation(self, date, time, state, people_quant, id_user):
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()

        # Consulta SQL para insertar una nueva reserva
        sql_query = """
            INSERT INTO Reservaciones (hora, fecha, estado, people_quant, id_usuario)
            VALUES (?, ?, ?, ?, ?)
        """

        try:
            # Ejecutar la consulta SQL con los parámetros proporcionados
            cursor.execute(sql_query, (time, date, self.set_state(state), people_quant, id_user))
            conn.commit()  # Confirmar la transacción
            print("Reserva insertada exitosamente.")
        except pyodbc.Error as e:
            conn.rollback()  # Revertir la transacción si hay un error
            print(f"Error al insertar la reserva: {e}")

        cursor.close()
        conn.close()


    def edit_reservation(self, reservation_id, state, people_quant, id_user):
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()

        # Consulta SQL para actualizar una reserva existente
        sql_query = """
            UPDATE Reservaciones
            SET estado = ?,
                people_quant = ?,
                id_usuario = ?
            WHERE id = ?
        """

        try:
            # Ejecutar la consulta SQL con los parámetros proporcionados
            cursor.execute(sql_query, (self.set_state(state), people_quant, id_user, reservation_id))
            conn.commit()  # Confirmar la transacción
            print(f"Reserva con ID {reservation_id} actualizada exitosamente.")
        except pyodbc.Error as e:
            conn.rollback()  # Revertir la transacción si hay un error
            print(f"Error al actualizar la reserva: {e}")

        cursor.close()
        conn.close()


    def getByIdUser(self, id_user):
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()
        
        sql_query = "SELECT * FROM Reservaciones WHERE id_usuario = ?"
        cursor.execute(sql_query, id_user)
        reservations = cursor.fetchall()

        #print(reservations)
        result = []

        # Procesar cada tupla de datos y convertir en formato JSON
        for item in reservations:
            id_str, time_str, date_str, is_free, people_quant, id_user = item
            time_formatted = time_str.split('.')[0]  # Obtener solo la hora sin microsegundos
            state = self.get_state(is_free)
            
            # Construir el objeto JSON para cada elemento
            json_obj = {
                "Id" : id_str,
                "Date": date_str,
                "Time": time_formatted,
                "State": state,
                "people_quant": people_quant,
                "id_user": id_user
            }
            result.append(json_obj)
            
            # Agregar el objeto JSON al resultado
        #print(result)
        cursor.close()
        conn.close()

        return result
        
        
