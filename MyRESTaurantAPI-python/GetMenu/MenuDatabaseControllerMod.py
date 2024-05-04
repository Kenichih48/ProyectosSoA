import json
import pyodbc


class MenuDatabaseController:
    """
    Controller for accessing menu data.
    """
    
    def __init__(self):
        """
        Initializes MenuDatabaseController with the file path.

        Parameters:
            file_path (str): The file path for the menu data.
        """

        server = 'DESKTOP-LMJ5G1R\\SQLEXPRESS'  # Nombre del servidor y nombre de instancia (si es necesario)
        database = 'MyRestaurantDataBase'  # Nombre de la base de datos
        username = 'INTEL'  # Nombre de usuario
        password = ''  # Contraseña

        self.conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes;'

        

    def get_menu(self):
        """
        Retrieves the entire menu.

        Returns:
            str: A JSON string representing the entire menu.
        """
        conn = pyodbc.connect(self.conn_str)
        
        cursor = conn.cursor()
        sql_query = """
            SELECT 
                P.nombre AS Nombre_Platillo,
                P.descripcion AS Descripcion_Platillo,
                R.set_rec AS Set_Recomendado,
                T.tipo AS Tipo_Platillo
            FROM 
                Recomendaciones R
            INNER JOIN 
                Platillos P ON R.id_platillo = P.id
            INNER JOIN 
                Tipo_Platillos T ON P.tipo_id = T.id;
        """
        cursor.execute(sql_query)
        menu = cursor.fetchall()

        sets_quant_ref = len(menu)/2
        sets_quant = sets_quant_ref
        
        menu_set = []
        menu_set_current = []
        
        for platillo in menu:
            
            menu_set_current += [platillo]
            sets_quant -= 1
            if sets_quant == 0:
                sets_quant = sets_quant_ref
                menu_set += [menu_set_current]
                menu_set_current = []
            

        # Lista para almacenar cada set como un objeto JSON
        result_sets = []
        
        for set_platillos in menu_set:
            # Diccionario para almacenar los platillos de cada tipo
            set_info = {
                'dish': None,
                'drink': None,
                'dessert': None
            }

            # Iterar sobre cada tupla en el set de platillos
            for platillo in set_platillos:
                name, description, set_rec, tipo = platillo
                if tipo == 'dish':
                    set_info['dish'] = {
                        'name': name,
                        'description': description
                    }
                elif tipo == 'drink':
                    set_info['drink'] = {
                        'name': name,
                        'description': description
                    }
                elif tipo == 'dessert':
                    set_info['dessert'] = {
                        'name': name,
                        'description': description
                    }
            
            # Agregar el set de platillos al resultado
            result_sets.append(set_info)

        # Convertir la lista de sets en formato JSON
        json_data = result_sets

        # Imprimir el JSON generado
        #print(json_data)
        
        cursor.close()
        conn.close()

        return json_data
        


