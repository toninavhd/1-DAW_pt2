CREATE DATABASE EMPRESA
GO
/*Creación de tabla EMPLE*/
IF OBJECT_ID('EMPLE') IS NOT NULL
DROP TABLE EMPLE
GO
CREATE TABLE EMPLE (
emp_no INTEGER NOT NULL,
apellido VARCHAR(50) NOT NULL,
oficio VARCHAR(20) NOT NULL,
dir INTEGER,
fecha_alt DATE NOT NULL,
salario INTEGER NOT NULL,
comision INTEGER,
departamento VARCHAR(20) NOT NULL,
CONSTRAINT pk_EMPLE PRIMARY KEY(emp_no));

/*Insertamos registros tabla EMPLE*/
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,departamento) values (7369,'SÁNCHEZ','EMPLEADO',7902,'17/12/1990',2040,'INVESTIGACION');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,departamento) values(7566,'JIMÉNEZ','DIRECTOR',7839,'02/04/1991',3867,'INVESTIGACION');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,departamento) values(7698,'NEGRO','DIRECTOR',7839,'01/05/1991',3705,'VENTAS');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,departamento) values(7788,'GIL','ANALISTA',7566,'09/11/1991',3900,'INVESTIGACION');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,departamento) values(7876,'ALONSO','EMPLEADO',7788,'23/09/1991',1430,'INVESTIGACION');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,departamento) values(7900,'JIMENO','EMPLEADO',7698,'03/12/1991',12350,'VENTAS');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,departamento) values(7902,'FERNÁNDEZ','ANALISTA',7566,'03/12/1991',3900,'INVESTIGACION');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,departamento) values(7934,'MUÑOZ','EMPLEADO',7782,'23/01/1992',1690,'CONTABILIDAD');
INSERT INTO EMPLE (emp_no,apellido,oficio,fecha_alt,salario,departamento) values(7839,'REY','PRESIDENTE','17/11/1991',65000,'CONTABILIDAD');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,comision,departamento) values(7499,'ARROYO','VENDEDOR',7698,'20/02/1995',2080,3900,'VENTAS');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,comision,departamento) values(7521,'SALA','VENDEDOR',7698,'22/02/1991',1625,16250,'VENTAS');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,comision,departamento) values(7654,'MARTÍN','VENDEDOR',7698,'29/09/1994',1625,182000,'VENTAS');
INSERT INTO EMPLE (emp_no,apellido,oficio,dir,fecha_alt,salario,comision,departamento) values(7844,'TOVAR','VENDEDOR',7698,'08/09/1996',1950,0,'VENTAS');
--
--INSERTAR LOS REGISTROS
/*Insertamos registros tabla DEPART*/
INSERT INTO DEPART values('CONTABILIDAD','SEVILLA');
INSERT INTO DEPART values('INVESTIGACION','MADRID');
INSERT INTO DEPART values('VENTAS','BARCELONA');
INSERT INTO DEPART values('PRODUCCION','BILBAO');

/* 1 Crea la tabla DEPART con los siguientes campos: */
CREATE TABLE DEPART (
    Dep_no INT IDENTITY(10, 10) PRIMARY KEY,
    Dnombre VARCHAR(20) NOT NULL,
    Loc VARCHAR(20) NOT NULL
);
--INSERTS de los registros
INSERT INTO DEPART values('CONTABILIDAD','SEVILLA');
INSERT INTO DEPART values('INVESTIGACION','MADRID');
INSERT INTO DEPART values('VENTAS','BARCELONA');
INSERT INTO DEPART values('PRODUCCION','BILBAO');
-- comprobación
SELECT * FROM DEPART;

/* 2 Modificar la localización del departamento que tiene una ‘O’ en el tercer carácter y una ‘D’ en el cuarto. La nueva localización es ‘VALENCIA’. Mostrar los datos de la tabla antes y después de la modificación*/
-- Modificar la localización
UPDATE DEPART
SET Loc = 'VALENCIA'
WHERE Dnombre LIKE '__OD%';

-- Volvemos a comprobar con SELECT
SELECT * FROM DEPART;

/*3- Mostrar en una sola columna calculada el apellido de los empleados seguido de
la cadena ‘de oficio: ‘ seguido del oficio, seguido de la cadena ‘y salario: ‘ seguido del
salario. Para los empleados que en el segundo caracter de su apellido tengan una letra
fuera del rango de la ‘A’ a la ‘K’. Ponerle nombre a la columna calculada.*/

SELECT 
    CONCAT(Apellido, ' de oficio: ', Oficio, ' y salario: ', Salario) AS Descripcion
FROM 
    EMPLE
WHERE 
    SUBSTRING(Apellido, 2, 1) NOT BETWEEN 'A' AND 'K';

/* 4- Mostrar el apellido y el año de alta de los empleados de oficio ‘vendedor’ o
‘analista’ . Sacar el listado ordenado por el año de alta. */

SELECT Apellido, YEAR(fecha_alt) AS AnioAlta
FROM EMPLE
WHERE Oficio IN ('vendedor', 'analista')
ORDER BY AnioAlta;

/* 5- Mostrar apellido, salario, comisión y mes de alta de los empleados que se
dieron de alta entre enero y julio.*/

SELECT Apellido, Salario, Comision, MONTH(fecha_alt)
FROM EMPLE
WHERE MONTH(fecha_alt) BETWEEN 1 AND 7;


/* 6- Cuántas personas trabajan en el departamento de ‘INVESTIGACION’, cuántas
cobran comisión y cuántos oficios hay.*/

-- Número de personas en el departamento de 'INVESTIGACION'
SELECT COUNT(*) AS NumeroPersonas
FROM EMPLE
WHERE Departamento = 'INVESTIGACION';

-- Número de personas que cobran comisión en el departamento de 'INVESTIGACION'
SELECT COUNT(*) AS NumeroComision
FROM EMPLE
WHERE Departamento = 'INVESTIGACION' AND Comision IS NOT NULL;

-- Número de oficios en el departamento de 'INVESTIGACION'
SELECT COUNT(DISTINCT Oficio) AS NumeroOficios
FROM EMPLE
WHERE Departamento = 'INVESTIGACION';

/* 7- Cuántos empleados hay en el departamento que tiene el salario más alto.*/

SELECT COUNT(*) AS NumeroEmpleados
FROM EMPLE
WHERE Departamento = (
    SELECT TOP 1 Departamento
    FROM EMPLE
    GROUP BY Departamento
    ORDER BY MAX(Salario) DESC
);

/* 8- Cuántos oficios hay por departamento, cuantos empleados cobran comisión y
media de salario.*/

SELECT Departamento, 
       COUNT(DISTINCT Oficio) AS NumeroOficios, 
       COUNT(Comision) AS NumeroComision,
       AVG(Salario) AS MediaSalario
FROM EMPLE
GROUP BY Departamento;


/*9- Departamento con mayor media de salario*/

SELECT top 1 Departamento, AVG(salario) as Media
FROM EMPLE
GROUP BY departamento
ORDER BY Media DESC;

/*10- Dar para cada oficio de los que tienen una media de salario mayor de 3000 el
total de empleados de dicho oficio y el número de empleados con comisión.
Ordenarlos de más a menos empleado*/

SELECT COUNT(*), 
    AVG(salario) as avgSalario,
    Comision
FROM EMPLE
HAVING AVG(salario) > 3000
ORDER BY avgSalario DESC
