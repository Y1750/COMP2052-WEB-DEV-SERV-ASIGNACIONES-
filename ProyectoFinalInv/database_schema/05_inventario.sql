DROP DATABASE IF EXISTS inventario;
CREATE DATABASE inventario DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE inventario;

-- Tabla de roles
CREATE TABLE role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64) NOT NULL UNIQUE
);

-- Tabla de usuarios
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(256) NOT NULL,
    role_id INT NOT NULL,
    FOREIGN KEY (role_id) REFERENCES role(id)
);

-- Tabla de ítems
CREATE TABLE item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL, -- ✅ Agregado
    categoria VARCHAR(50) NOT NULL,
    cantidad INT NOT NULL,
    precio_estimado DECIMAL(10,2),
    ubicacion VARCHAR(100),
    fecha_adquisicion DATE,
    owner_id INT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES user(id)
);
