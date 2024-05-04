
-- Crear la base de datos
CREATE DATABASE MyRestaurantDataBase;

-- Usar la base de datos restaurante
USE MyRestaurantDataBase;

-- Crear la tabla Usuario
CREATE TABLE Usuario (
    id INT IDENTITY(1,1) PRIMARY KEY,
    contraseņa VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
	nivel_acceso BIT NOT NULL,
);

-- Crear la tabla Reservaciones
CREATE TABLE Reservaciones (
    id INT IDENTITY(1,1) PRIMARY KEY,
    hora TIME NOT NULL,
    fecha DATE NOT NULL,
	estado BIT NOT NULL
);


-- Crear la tabla TIPO_Platillos
CREATE TABLE Tipo_Platillos(

	id INT IDENTITY(1,1) PRIMARY KEY,
	tipo VARCHAR(50)

);

-- Crear la tabla Platillos
CREATE TABLE Platillos (
    id INT IDENTITY(1,1) PRIMARY KEY,
	tipo_id INT,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(255)
	FOREIGN KEY (tipo_id) REFERENCES Tipo_Platillos(id)
);

-- Crear la tabla Recomendaciones
CREATE TABLE Recomendaciones (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_platillo INT,
    set_rec INT,
    FOREIGN KEY (id_platillo) REFERENCES Platillos(id)
);



