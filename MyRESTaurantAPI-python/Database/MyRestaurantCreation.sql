
-- Crear la base de datos
CREATE DATABASE MyRestaurantDataBase;

-- Usar la base de datos restaurante
USE MyRestaurantDataBase;

-- Crear la tabla Usuario
CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contrasena VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    nivel_acceso TINYINT(1) NOT NULL
);

-- Crear la tabla Reservaciones
CREATE TABLE Reservaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hora TIME NOT NULL,
    fecha DATE NOT NULL,
    estado TINYINT(1) NOT NULL,
    people_quant INT,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id)
);

-- Crear la tabla Tipo_Platillos
CREATE TABLE Tipo_Platillos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50)
);

-- Crear la tabla Platillos
CREATE TABLE Platillos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_id INT,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(255),
    FOREIGN KEY (tipo_id) REFERENCES Tipo_Platillos(id)
);

-- Crear la tabla Recomendaciones
CREATE TABLE Recomendaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_platillo INT,
    set_rec INT,
    FOREIGN KEY (id_platillo) REFERENCES Platillos(id)
);



