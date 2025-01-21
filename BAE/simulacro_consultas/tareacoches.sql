-- Ejercicio de consultas múltiples y uniones segunda parte


--1 Crear la Base de datos AlquilerCochesSinFK, sus tablas y cargarlas con datos a partir del archivo suministrado.
ALTER TABLE Alquiler CHECK CONSTRAINT fk_coche;
--2 Crear las Foreign Key correspondientes al esquema siguiente:
INSERT INTO Alquiler (id, id_cliente, id_coche, fecha_alquiler, fecha_devolucion) VALUES (4, 1, 999, '2025-01-21', '2025-01-28');
-- Esto debería fallar debido a la restricción de clave foránea

--3.- Insertar un coche de un tipo diferente a los existentes en tipocoche.
ALTER TABLE Alquiler DROP CONSTRAINT fk_coche;
--4 Insertar un coche con tipo NULL.
ALTER TABLE Alquiler
ADD CONSTRAINT fk_coche FOREIGN KEY (id_coche) REFERENCES Coche(id);
GO
--5.- Alquilar un coche existente a un cliente no existente.
DELETE FROM Alquiler WHERE id_coche NOT IN (SELECT id FROM Coche);
GO

ALTER TABLE Alquiler
ADD CONSTRAINT fk_coche FOREIGN KEY (id_coche) REFERENCES Coche(id);
GO

--6- Realizar un alquiler correcto.
ALTER TABLE Alquiler
ADD CONSTRAINT fk_coche FOREIGN KEY (id_coche) REFERENCES Coche(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
GO

--7.- Ver la información de las restricciones activas en la tabla alq_alquiler
DELETE FROM Coche WHERE id = 1;
GO

--8.- Intentar borrar un coche con alquileres
UPDATE Coche SET id = 10 WHERE id = 1;
GO

--9.- Deshabilitar la FK de alquiler relacionada con coche.
CREATE DATABASE AlquilerCochesConFK;
GO
USE AlquilerCochesConFK;
GO

CREATE TABLE Cliente (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    direccion VARCHAR(255)
);
GO

CREATE TABLE Coche (
    id INT PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    tipo VARCHAR(50)
);
GO

CREATE TABLE Alquiler (
    id INT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_coche INT NOT NULL,
    fecha_alquiler DATE,
    fecha_devolucion DATE,
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
    CONSTRAINT fk_coche FOREIGN KEY (id_coche) REFERENCES Coche(id)
);
GO

-- 10.- Insertar un alquiler a un cliente existente de un coche no existente.
INSERT INTO Coche (id, marca, modelo, tipo) VALUES (6, 'Chevrolet', 'Camaro', NULL);
-- Esto debería fallar si el campo 'tipo' no permite valores NULL
GO

--11.- Habilitar la restricción.
ALTER TABLE Alquiler CHECK CONSTRAINT fk_coche;
GO

--12.- Volver a intentar insertar un alquiler a un cliente existente de un coche no existente.
INSERT INTO Alquiler (id, id_cliente, id_coche, fecha_alquiler, fecha_devolucion) VALUES (4, 1, 999, '2025-01-21', '2025-01-28');
-- Esto debería fallar debido a la restricción de clave foránea
GO

--13.- Borrar la restricción.
ALTER TABLE Alquiler DROP CONSTRAINT fk_coche;
GO

--14.- Crear de nuevo la restricción.

ALTER TABLE Alquiler
ADD CONSTRAINT fk_coche FOREIGN KEY (id_coche) REFERENCES Coche(id);
GO

--15.- ¿Cómo podemos hacer para crear de nuevo la restricción? Borrar al final los datos descuadrados
DELETE FROM Alquiler WHERE id_coche NOT IN (SELECT id FROM Coche);
GO

--16.- Crear la restricción activando borrados y actualizaciones en cascada.
ALTER TABLE Alquiler
ADD CONSTRAINT fk_coche FOREIGN KEY (id_coche) REFERENCES Coche(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
GO

--17.- Borrar un coche con alquileres y ver lo que ocurre con sus alquileres.

DELETE FROM Coche WHERE id = 1;
GO

--18.- Modificar la matrícula de un coche con alquileres y ver lo que pasa con sus alquileres.

UPDATE Coche SET id = 10 WHERE id = 1;
GO

--19.- Cómo modificaríamos la creación de las tablas para colocarle las foreign key y evitar que puedan colocarse valores null en los campos correspondientes a las mismas. Crear de nuevo la BD con ese cambio.

CREATE DATABASE AlquilerCochesConFK;
GO
USE AlquilerCochesConFK;
GO

CREATE TABLE Cliente (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    direccion VARCHAR(255)
);
GO

CREATE TABLE Coche (
    id INT PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    tipo VARCHAR(50)
);
GO

CREATE TABLE Alquiler (
    id INT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_coche INT NOT NULL,
    fecha_alquiler DATE,
    fecha_devolucion DATE,
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
    CONSTRAINT fk_coche FOREIGN KEY (id_coche) REFERENCES Coche(id)
);
GO

--20.- Probar una inserción de un coche con tipocoche a null.

INSERT INTO Coche (id, marca, modelo, tipo) VALUES (6, 'Chevrolet', 'Camaro', NULL);
-- Esto debería fallar si el campo 'tipo' no permite valores NULL
GO

