-- Insertar tipos de platillos en Tipo_Platillos
INSERT INTO Tipo_Platillos (id, tipo) VALUES
(1, 'fuerte'),
(2, 'bebida'),
(3, 'postre');

-- Insertar platillos en la tabla Platillos (uno de cada tipo)
-- Platillo fuerte
INSERT INTO Platillos (id, tipo_id, nombre, descripcion) VALUES
(1, 1, 'Filete de res', 'Filete de res a la parrilla con guarnici�n de verduras.');

-- Platillo bebida
INSERT INTO Platillos (id, tipo_id, nombre, descripcion) VALUES
(2, 2, 'Margarita', 'C�ctel Margarita con tequila, triple sec y jugo de lim�n.');

-- Platillo postre
INSERT INTO Platillos (id, tipo_id, nombre, descripcion) VALUES
(3, 3, 'Tarta de Chocolate', 'Deliciosa tarta de chocolate con crema batida.');

-- Insertar recomendaciones en la tabla Recomendaciones (todos con el mismo set_rec)
INSERT INTO Recomendaciones (id, id_platillo, set_rec) VALUES
(1, 1, 1),  -- Recomendaci�n de platillo fuerte (id_platillo = 1)
(2, 2, 1),  -- Recomendaci�n de platillo bebida (id_platillo = 2)
(3, 3, 1);  -- Recomendaci�n de platillo postre (id_platillo = 3)


-- Insertar platillos adicionales en la tabla Platillos (uno de cada tipo)
-- Platillo fuerte
INSERT INTO Platillos (id, tipo_id, nombre, descripcion) VALUES
(4, 1, 'Pollo al Curry', 'Pollo cocinado en una salsa de curry con arroz basmati.');

-- Platillo bebida
INSERT INTO Platillos (id, tipo_id, nombre, descripcion) VALUES
(5, 2, 'Pi�a Colada', 'C�ctel tropical con ron, crema de coco y jugo de pi�a.');

-- Platillo postre
INSERT INTO Platillos (id, tipo_id, nombre, descripcion) VALUES
(6, 3, 'Cheesecake de Fresa', 'Cheesecake con base de galleta y cubierta de fresas frescas.');

-- Insertar recomendaciones adicionales en la tabla Recomendaciones (todos con el mismo set_rec)
INSERT INTO Recomendaciones (id, id_platillo, set_rec) VALUES
(4, 4, 2),  -- Recomendaci�n de otro platillo fuerte (id_platillo = 4)
(5, 5, 2),  -- Recomendaci�n de otra bebida (id_platillo = 5)
(6, 6, 2);  -- Recomendaci�n de otro postre (id_platillo = 6)



-- Poblar la tabla Usuario
INSERT INTO Usuario (id, contrase�a, correo, nombre, apellido, direccion) VALUES
(1, 'clave123', 'usuario1@example.com', 'Juan', 'P�rez', 'Calle Principal #123'),
(2, 'contrase�a456', 'usuario2@example.com', 'Mar�a', 'Garc�a', 'Avenida Central #456'),
(3, 'password789', 'usuario3@example.com', 'Pedro', 'L�pez', 'Calle Secundaria #789');

-- Poblar la tabla Reservaciones
INSERT INTO Reservaciones (id, hora, fecha, estado) VALUES
(1, '18:00:00', '2024-05-05', 0),
(2, '19:30:00', '2024-05-10', 0),
(3, '20:00:00', '2024-05-15', 1);

