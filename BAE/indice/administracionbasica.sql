-- 2. Crear una tabla con la estructura siguiente:

CREATE TABLE empleados (
    --a) El DNI debe ser un número de 8 dígitos.
    DNI VARCHAR(8) PRIMARY KEY,
    
    --b) El nombre y los apellidos deben tener entre 3 y 30 caracteres.
    nombre VARCHAR(30) NOT NULL,
    apellidos VARCHAR(30) NOT NULL,
    
    --c) La fecha de nacimiento debe ser menor que la fecha actual.
    fechanacimiento DATETIME CHECK (fechanacimiento < CURRENT_DATE),
    
    --d) La cantidad de hijos debe ser un número entero entre 0 y 20.
    cantidadhijos TINYINT CHECK (cantidadhijos >= 0 AND cantidadhijos <= 20),

    --e) La sección debe tener entre 3 y 20 caracteres
    seccion VARCHAR(20) NOT NULL,

    --f) El sueldo debe ser un número decimal con 2 decimales.
    sueldo DECIMAL(6,2),
    UNIQUE (DNI)
);

--3 Crear las sentencias para que valide lo siguiente:
--a) El DNI debe ser un número de 8 dígitos.
--b) El nombre y los apellidos deben tener entre 3 y 30 caracteres.
--c) La fecha de nacimiento debe ser menor que la fecha actual.
--d) La cantidad de hijos debe ser un número entero entre 0 y 20.
--e) La sección debe tener entre 3 y 20 caracteres.
--f) El sueldo debe ser un número decimal con 2 decimales.