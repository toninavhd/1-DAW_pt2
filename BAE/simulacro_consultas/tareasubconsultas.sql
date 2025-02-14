create database Subconsultas
go

use Subconsultas
go

create table empleado(
		emp_no 	INTEGER PRIMARY KEY,
	apellido VARCHAR(50) NOT NULL,
	oficio VARCHAR(30),
	dir INTEGER,
	fecha_alt DATE,
		salario INTEGER,
		comision INTEGER,	
		dept_no INTEGER);	

create table departa(

        dept_no INTEGER,
	dnombre VARCHAR(30),
	loc VARCHAR(30));


INSERT INTO empleado VALUES (7329,'SANCHEZ','OFICINISTA',7902,'1990/12/17',
                        800,NULL,20);
INSERT INTO empleado VALUES (7499,'ARROYO','VENDEDOR',7698,'1990/02/20',
                        1600,300,30);
INSERT INTO empleado VALUES (7521,'SALA','VENDEDOR',7698,'1991/02/22',
                        1250,500,30);
INSERT INTO empleado VALUES (7566,'JIMENEZ','GERENTE',7839,'1991/04/02',
                        2975,NULL,20);
INSERT INTO empleado VALUES (7654,'MARTÍN','VENDEDOR',7698,'1991/09/29',
                        1250,1400,30);
INSERT INTO empleado VALUES (7698,'NEGRO','GERENTE',7839,'1991/05/01',
                        2850,NULL,30);
INSERT INTO empleado VALUES (7782,'CEREZO','GERENTE',7839,'1991/06/09',
                       2450,NULL,10);
INSERT INTO empleado VALUES (7788,'GIL','ANALISTA',7566,'1991/11/09',
                        3000,NULL,20);
INSERT INTO empleado VALUES (7839,'REY','PRESIDENTE',NULL,'1991/11/17',
                        5000,NULL,10);
INSERT INTO empleado VALUES (7844,'TOVAR','VENDEDOR',7698,'1991/09/08',
                        1500,0,30);
INSERT INTO empleado VALUES (7876,'ALONSO','OFICINISTA',7788,'1991/09/23',
                        1100,NULL,20);
INSERT INTO empleado VALUES (7900,'JIMENO','OFICINISTA',7698,'1991/12/03',
                        950,NULL,30);
INSERT INTO empleado VALUES (7902,'FERNANDEZ','ANALISTA',7566,'1991/12/03',
                        3000,NULL,20);
INSERT INTO empleado VALUES (7934,'MUÑOZ','OFICINISTA',7782,'1992/01/23',
                        1300,NULL,10);

INSERT INTO departa VALUES (10,'CONTABILIDAD','SEVILLA');
INSERT INTO departa VALUES (20,'INVESTIGACIÓN','MADRID');
INSERT INTO departa VALUES (30,'VENTAS','BARCELONA');
INSERT INTO departa VALUES (40,'PRODUCCIÓN','BILBAO');

-- 1. Listar apellido y nombre del departamento de todos aquellos empleados que trabajan en departamentos que no están ni en Madrid ni en Barcelona. Ordenados por apellidos de forma descendente.

SELECT apellido, dnombre
FROM empleado, departa
WHERE empleado.dept_no = departa.dept_no
AND loc NOT IN ('MADRID','BARCELONA')
ORDER BY apellido DESC;

-- 2. Listar apellidos y oficio de todos aquellos empleados que tiene el mismo oficio que JIMENEZ, no se incluye a JIMENEZ.  Ordenados por apellidos de forma descendente.

SELECT apellido, oficio
FROM empleado
WHERE oficio = (SELECT oficio
FROM empleado
WHERE apellido = 'JIMENEZ')
AND apellido != 'JIMENEZ'
ORDER BY apellido DESC;

-- 3. Listar el salario, oficio, apellido, y número de departamento de todos aquellos empleados que cobren más que algún empleado del departamento 30. Ordenados en orden decreciente de salarios.

SELECT salario, oficio, apellido, dept_no
FROM empleado
WHERE salario > ANY (SELECT salario
FROM empleado
WHERE dept_no = 30)
ORDER BY salario DESC;

-- 4. Listar salario, oficio, apellido y número de departamento de todos aquellos empleados que cobren más que (todos) cualquiera de los empleados del departamento 30.Ordenados en orden decreciente de salarios. 

SELECT salario, oficio, apellido, dept_no
FROM empleado
WHERE salario > ALL (SELECT salario
FROM empleado
WHERE dept_no = 30)
ORDER BY salario DESC;

-- 5. Listar apellidos y oficio de los de empleado del departamento 10 que tengan un oficio realizado  por alguna persona del departamento 30.

SELECT e1.apellido, e1.oficio
FROM empleado e1, empleado e2
WHERE e1.dept_no = 10
AND e2.dept_no = 30
AND e1.oficio = e2.oficio;

-- 6. Listar apellido y nombre de departamento de los empleados que tiene como jefe a NEGRO. Ordenados por Apellidos en orden decreciente.

SELECT e.apellido, d.dnombre
FROM empleado e
JOIN departa d ON e.dept_no = d.dept_no
WHERE e.dir = (SELECT emp_no FROM empleado WHERE apellido = 'NEGRO')
ORDER BY e.apellido DESC;

-- 7. Listar los apellido, oficio y salario de los empleados que tienen el mismo oficio y salario que  FERNANDEZ.

SELECT e.apellido, e.oficio, e.salario
FROM empleado e
WHERE e.oficio = (SELECT oficio FROM empleado WHERE apellido = 'FERNANDEZ')
AND e.salario = (SELECT salario FROM empleado WHERE apellido = 'FERNANDEZ');

-- 8. listar apellido, oficio, Nombre departamento y salario de todos aquellos empleados que tienen el mismo trabajo que JIMENEZ o bien un sueldo mayor o igual que FERNANDEZ, ordenar la salida por orden alfabético de oficio y por salarios decrecientes.

SELECT e.apellido, e.oficio, d.dnombre, e.salario
FROM empleado e
JOIN departa d ON e.dept_no = d.dept_no
WHERE e.oficio = (SELECT oficio FROM empleado WHERE apellido = 'JIMENEZ')
OR e.salario >= (SELECT salario FROM empleado WHERE apellido = 'FERNANDEZ')
ORDER BY e.oficio ASC, e.salario DESC;

-- 9. Lista el apellido y oficio de aquellos empleados del departamento 10 que tengan un oficio similar al realizado por alguna persona del departamento VENTAS.

SELECT e1.apellido, e1.oficio
FROM empleado e1
WHERE e1.dept_no = 10
AND e1.oficio IN (SELECT e2.oficio
FROM empleado e2
JOIN departa d ON e2.dept_no = d.dept_no
WHERE d.dnombre = 'VENTAS');

--10. Listar el nombre del departamento, apellido y salario de aquellos empleados que ganan más que el salario medio de su departamento, ordenar por nombre del departamento.

SELECT d.dnombre, e.apellido, e.salario
FROM empleado e
JOIN departa d ON e.dept_no = d.dept_no
WHERE e.salario > (SELECT AVG(e2.salario)
FROM empleado e2
WHERE e2.dept_no = e.dept_no)
ORDER BY d.dnombre;

