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
    seccion VARCHAR(20) CHECK != '',

    --f) El sueldo debe ser un número decimal con 2 decimales.
    sueldo DECIMAL(6,2),
    UNIQUE (apellidos, nombre)
);

--4. Ver los índices que tiene.

-- 5. Añadir índice por fecha de nacimiento
CREATE INDEX idx_fechanacimiento ON empleados (fechanacimiento);

-- 6. Añadir índice por sueldo
CREATE INDEX idx_sueldo ON empleados (sueldo);

-- 7. Modificar lo siguiente en la tabla
--a. Añadir campo dirección varchar(100)
ALTER TABLE empleados ADD COLUMN direccion VARCHAR(100);

-- b. Cambiar a no nulo seccion
ALTER TABLE empleados ALTER COLUMN seccion SET NOT NULL;

-- c. Validar que sueldo sean >0 y <10000
ALTER TABLE empleados ADD CONSTRAINT chk_sueldo CHECK (sueldo > 0 AND sueldo
< 10000);