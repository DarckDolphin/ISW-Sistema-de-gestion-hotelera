-- Creación de la base de datos
CREATE DATABASE gestion_hotelera;

-- Conexión a la base de datos
\c gestion_hotelera;

-- Tabla de Hotel
CREATE TABLE Hotel (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion TEXT NOT NULL,
    clasificacion INT CHECK (clasificacion BETWEEN 1 AND 5),
    numero_habitaciones INT NOT NULL
);

-- Tabla de Habitación
CREATE TABLE Habitacion (
    id SERIAL PRIMARY KEY,
    numero_habitacion INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    precio_por_noche DECIMAL(10, 2) NOT NULL,
    estado VARCHAR(50) DEFAULT 'disponible',
    hotel_id INT REFERENCES Hotel(id) ON DELETE CASCADE
);

-- Tabla de Huésped
CREATE TABLE Huesped (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    documento_identidad VARCHAR(20) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    correo_electronico VARCHAR(100)
);

-- Tabla de Reserva
CREATE TABLE Reserva (
    id SERIAL PRIMARY KEY,
    fecha_entrada DATE NOT NULL,
    fecha_salida DATE NOT NULL,
    numero_huespedes INT NOT NULL,
    estado VARCHAR(50) DEFAULT 'pendiente',
    huesped_id INT REFERENCES Huesped(id) ON DELETE CASCADE,
    habitacion_id INT REFERENCES Habitacion(id) ON DELETE SET NULL
);

-- Tabla de Servicio
CREATE TABLE Servicio (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL
);

-- Tabla para asociar servicios a reservas
CREATE TABLE Reserva_Servicio (
    id SERIAL PRIMARY KEY,
    reserva_id INT REFERENCES Reserva(id) ON DELETE CASCADE,
    servicio_id INT REFERENCES Servicio(id) ON DELETE CASCADE,
    cantidad INT DEFAULT 1
);

-- Tabla de Empleado
CREATE TABLE Empleado (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    puesto VARCHAR(100) NOT NULL,
    telefono VARCHAR(15),
    correo_electronico VARCHAR(100)
);

-- Tabla de Factura
CREATE TABLE Factura (
    id SERIAL PRIMARY KEY,
    fecha_emision DATE NOT NULL,
    importe_total DECIMAL(10, 2) NOT NULL,
    metodo_pago VARCHAR(50),
    reserva_id INT REFERENCES Reserva(id) ON DELETE SET NULL
);
