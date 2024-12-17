CREATE DATABASE INSTITUTO
GO
use INSTITUTO
go

if OBJECT_ID('alumnos') is not null
drop table alumnos

create table alumnos(
    expediente char(6) primary key,
	nombre varchar(50),
	localidad varchar(50),
	fecha_nac datetime,
	direccion varchar(50),
	curso int,
	nivel varchar(10),
	faltas int,
	beca int);
	

insert into alumnos values(123456,'Juan Miguel Soler Bakero','Murcia','10/10/07','Gran Via, 2, 4A',1,'ESO',15,200);
insert into alumnos values(654321,'Laura Gomez Fernandez','Lorca','10/05/06','Junterones, 10, 5B',2,'ESO',25,null);
insert into alumnos values(765432,'Beatriz Martinez Hernandez','Murcia','05/05/05','Plaza Mayor, 6, 3B',3,'ESO',5,null);
insert into alumnos values(987654,'Diego Marin Llorente','Alhama de Murcia','03/06/02','Diego de la Cierva, 5, 7A',1,'BACHILLER',34,null);
insert into alumnos values(445544,'Juan Francisco Cano Riquelme','Murcia','01/07/04','Plaza de Belluga, 3, 4A',4,'ESO',13,500);
insert into alumnos values(998867,'Leonor Sanchez Fernández','Murcia','03/01/04','Torre de Romo, 8',4,'ESO',5,null);
insert into alumnos values(223322,'Raquel Riquelme Rubio','Lorca','05/11/02','San Juan, 14, 3B',1,'BACHILLER',7,1000);
insert into alumnos values(998887,'Cristina Sanchez Bermejo','Murcia','03/10/07','Torre de Romo, 7',1,'ESO',1,null);
insert into alumnos values(334455,'Pedro Jesus Rodriguez Soler','Alhama de Murcia','10/03/06','Camino de Badel, 4',2,'ESO',11,750);
insert into alumnos values(334400,'Javier Ramonez Rodriguez','Murcia','05/02/05','Gran Va, 4, 3A',3,'ESO',0,null);
insert into alumnos values(993322,'Gema Rubio Colero','Lorca','09/09/04','Plaza Fuensanta, 5, 7A',1,'BACHILLER',19,1000);
insert into alumnos values(555511,'Joaquin Hernandez Gonzalez','Lorca','12/12/03','Junterones, 4, 5A',2,'BACHILLER',14,null);
insert into alumnos values(554477,'Marcos Lopez Gonzalez','Murcia','11/10/03','C/ Peñón 111, 1A',2,'BACHILLER',15,500);
insert into alumnos values(554444,'Gustavo Bueno Gonzalez','Murcia','11/10/04','C/ San Juan 12, 3A',1,'BACHILLER',15,750);

-- 1-Actualiza la tabla disminuyendo un 10% la beca de los alumnos que tienen más de 15 faltas. Mostrar el antes y el después.

SELECT * FROM alumnos 
WHERE faltas > 15;

-- Actualizada

UPDATE alumnos
SET beca = beca * 0.9
WHERE faltas > 15;

-- Volvemos a mirar usando la consulta anterior

SELECT * FROM alumnos 
WHERE faltas > 15;

-- 2- Listar los alumnos dando nombre, localidad curso y nivel, que contengan una ‘ez’ en su nombre y la localidad termine en ‘cia’. Ordenar por nivel de menor a mayor y por curso de menor a mayor.

SELECT nombre, localidad, curso, nivel
FROM alumnos
WHERE nombre LIKE '%ez%' AND localidad LIKE '%cia'
ORDER BY nivel, curso;

-- 3- Listar los alumnos hasta 3º de la ESO, dando el nombre en mayúsculas y en una sola columna el curso y nivel (pe: “3º de la ESO”). Darle nombre a la columna calculada

SELECT UPPER(Nombre) AS Nombre, CONCAT(Curso, ' de la ', Nivel) AS alumno_curso_UPPER
FROM Alumnos
WHERE Nivel = 'ESO' AND Curso <= 3;

-- 4 -Cuántos alumnos hay matriculados.

SELECT COUNT(*) FROM alumnos

-- 5 Cuántos alumnos hay por curso y nivel y cuántos tienen beca. Ordenados por curso y nivel de menor a mayor.

SELECT curso, nivel, COUNT(*) AS totalalumnos, SUM(beca) AS AlumnosBecados
FROM alumnos
GROUP BY curso, nivel
ORDER BY nivel, curso;

-- 6 Mostrar curso y nivel con una media de beca mayor que 200, mostrando el total de beca en cada curso y nivel.

SELECT curso, nivel, AVG(beca) AS media_beca, SUM(beca) AS beca_total
FROM alumnos
GROUP BY curso, nivel
HAVING AVG(beca) > 200;

--7 Mostrar los dos meses con más cumpleaños

SELECT TOP 2 MONTH(fecha_nac) AS mes, COUNT(*) AS TotalCumpleaños
FROM alumnos
GROUP BY MONTH(fecha_nac)
ORDER BY TotalCumpleaños DESC;

--8 Sacar un listado con los alumnos que no tienen beca mostrando nombre, edad y el día de la semana en que nacieron.

SELECT Nombre, DATEDIFF(YEAR, fecha_nac, GETDATE()) AS Edad, DATENAME(WEEKDAY, fecha_nac) AS DiaSemana
FROM Alumnos
WHERE Beca = 0;

--9 Alumnos entre 15 y 17 años, mostrar nombre y curso.

SELECT nombre, curso
FROM alumnos
WHERE DATEDIFF(YEAR, fecha_nac, GETDATE()) BETWEEN 15 AND 17;

--10 Curso con mayor numero de matriculados

SELECT TOP 1 curso AS curso, COUNT(*) AS total
FROM alumnos
GROUP BY curso
ORDER BY total DESC;

