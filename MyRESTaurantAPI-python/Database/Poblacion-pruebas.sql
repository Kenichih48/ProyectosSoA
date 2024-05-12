USE MyRestaurantDataBase;

-- Insertar tipos de platillos en Tipo_Platillos
INSERT INTO Tipo_Platillos (tipo) VALUES
('dish'),
('drink'),
('dessert');

-- Insertar platillos en la tabla Platillos (uno de cada tipo)
-- Platillo fuerte
INSERT INTO Platillos (tipo_id, nombre, descripcion) VALUES
(1, 'Filete de res', 'Filete de res a la parrilla con guarnición de verduras.');

-- Platillo bebida
INSERT INTO Platillos (tipo_id, nombre, descripcion) VALUES
(2, 'Margarita', 'Cóctel Margarita con tequila, triple sec y jugo de limón.');

-- Platillo postre
INSERT INTO Platillos (tipo_id, nombre, descripcion) VALUES
(3, 'Tarta de Chocolate', 'Deliciosa tarta de chocolate con crema batida.');

-- Insertar recomendaciones en la tabla Recomendaciones (todos con el mismo set_rec)
INSERT INTO Recomendaciones (id_platillo, set_rec) VALUES
(1, 1),  -- Recomendación de platillo fuerte (id_platillo = 1)
(2, 1),  -- Recomendación de platillo bebida (id_platillo = 2)
(3, 1);  -- Recomendación de platillo postre (id_platillo = 3)


-- Insertar platillos adicionales en la tabla Platillos (uno de cada tipo)
-- Platillo fuerte
INSERT INTO Platillos (tipo_id, nombre, descripcion) VALUES
(1, 'Pollo al Curry', 'Pollo cocinado en una salsa de curry con arroz basmati.');

-- Platillo bebida
INSERT INTO Platillos (tipo_id, nombre, descripcion) VALUES
(2, 'Piña Colada', 'Cóctel tropical con ron, crema de coco y jugo de piña.');

-- Platillo postre
INSERT INTO Platillos (tipo_id, nombre, descripcion) VALUES
(3, 'Cheesecake de Fresa', 'Cheesecake con base de galleta y cubierta de fresas frescas.');

-- Insertar recomendaciones adicionales en la tabla Recomendaciones (todos con el mismo set_rec)
INSERT INTO Recomendaciones (id_platillo, set_rec) VALUES
(4, 2),  -- Recomendación de otro platillo fuerte (id_platillo = 4)
(5, 2),  -- Recomendación de otra bebida (id_platillo = 5)
(6, 2);  -- Recomendación de otro postre (id_platillo = 6)



-- Poblar la tabla Usuario
INSERT INTO Usuario (contrasena, correo, nombre, apellido, direccion, nivel_acceso) VALUES
('clave123', 'usuario1@example.com', 'Juan', 'Pérez', 'Calle Principal #123', 1),
('contraseña456', 'usuario2@example.com', 'María', 'García', 'Avenida Central #456', 0),
('password789', 'usuario3@example.com', 'Pedro', 'López', 'Calle Secundaria #789', 0);


-- Poblar la tabla Reservaciones
INSERT INTO Reservaciones (hora, fecha, estado, people_quant, id_usuario) VALUES
('18:00:00', '2024-05-05', 1, 2, 1),
('19:30:00', '2024-05-10', 0, 0,NULL),
('20:00:00', '2024-05-15', 0, 0, NULL);


