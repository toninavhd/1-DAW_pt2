-- Crear la base de datos
CREATE DATABASE PrestamoLibros;
GO

-- Usar la base de datos
USE PrestamoLibros;
GO

-- Crear la tabla libros
IF OBJECT_ID('libros') IS NOT NULL
    DROP TABLE libros;
GO

CREATE TABLE libros (
    codigo INT IDENTITY,
    titulo VARCHAR(40) NOT NULL,
    autor VARCHAR(20) DEFAULT 'Desconocido',
    editorial VARCHAR(20),
    precio DECIMAL(6,2),
    cantidad TINYINT DEFAULT 0,
    PRIMARY KEY (codigo)
);
GO

-- Insertar datos en la tabla libros
INSERT INTO libros (titulo, autor, editorial, precio)
VALUES ('El aleph', 'Borges', 'Emece', 25.00);

INSERT INTO libros (titulo, autor, editorial, precio, cantidad)
VALUES ('Java en 10 minutos', 'Mario Molina', 'Siglo XXI', 50.40, 100);

INSERT INTO libros (titulo, autor, editorial, precio, cantidad)
VALUES ('Alicia en el pais de las maravillas', 'Lewis Carroll', 'Emece', 15.00, 50);
GO

-- Mostrar las 3 primeras letras de todos los títulos
SELECT LEFT(titulo, 3) AS 'Primeras 3 letras del título' FROM libros;
GO

-- Mostrar el precio como cadena de caracteres
SELECT CAST(precio AS VARCHAR) AS 'Precio como cadena' FROM libros;
GO

-- Mostrar la cadena con el título, un guión, el autor y el precio
SELECT CONCAT(titulo, ' - ', autor, ' - ', CAST(precio AS VARCHAR)) AS 'Título-Autor-Precio' FROM libros;
GO

-- Mostrar las seis últimas letras del título y del autor
SELECT RIGHT(titulo, 6) AS 'Últimas 6 letras del título', RIGHT(autor, 6) AS 'Últimas 6 letras del autor' FROM libros;
GO

-- Mostrar el nombre del autor en mayúscula
SELECT UPPER(autor) AS 'Autor en mayúscula' FROM libros;
GO

-- Indicar el número de letras del autor y del título
SELECT titulo, LEN(titulo) AS 'Número de letras del título', autor, LEN(autor) AS 'Número de letras del autor' FROM libros;
GO

-- Mostrar los caracteres del 4 al 10 del autor
SELECT SUBSTRING(autor, 4, 7) AS 'Caracteres del 4 al 10 del autor' FROM libros;
GO

-- Cambiar "arroba" por "@" y "punto" por "." en el texto "correoarrobahotmailpuntocom"
SELECT REPLACE(REPLACE('correoarrobahotmailpuntocom', 'arroba', '@'), 'punto', '.') AS 'Correo modificado';
GO
