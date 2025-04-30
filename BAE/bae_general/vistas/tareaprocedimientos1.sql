-- Ejercicio 1: Crear un procedimiento almacenado que contenga las siguientes instrucciones:
-- eliminación de la tabla "libros" si existe;
-- creación de la tabla "libros" con: codigo, titulo, autor, editorial, precio, cantidad;
-- ingreso de algunos registros.

if object_id('libros') is not null
drop table libros;

create table libros(
codigo int,
titulo varchar(50),
autor varchar(50),
editorial varchar(50),
precio decimal(10,2),
cantidad int
);

insert into libros values(1, 'Libro 1', 'Autor 1', 'Editorial 1', 100.00, 10);
insert into libros values(2, 'Libro 2', 'Autor 2', 'Editorial 2', 200.00, 20);
insert into libros values(3, 'Libro 3', 'Autor 3', 'Editorial 3', 300.00, 30);

-- Ejercicio 2: Crear un procedimiento almacenado que muestre los libros de los cuales hay menos de 10.

if object_id('pa_libros_menos_10') is not null
drop procedure pa_libros_menos_10;

create procedure pa_libros_menos_10
as
begin
select * from libros where cantidad < 10;
end;

exec pa_libros_menos_10;

-- Ejercicio 3: Crear un procedimiento almacenado que seleccione los nombres, apellidos y sueldos de los empleados que tengan un sueldo superior o igual al enviado como parámetro.

if object_id('pa_empleados_sueldo') is not null
drop procedure pa_empleados_sueldo;

create procedure pa_empleados_sueldo
@sueldo decimal(10,2)
as
begin
select nombre, apellido, sueldo from empleados where sueldo >= @sueldo;
end;

exec pa_empleados_sueldo 400;
exec pa_empleados_sueldo 500;

-- Ejercicio 4: Crear un procedimiento almacenado que actualice los sueldos iguales al enviado como primer parámetro con el valor enviado como segundo parámetro.

if object_id('pa_empleados_actualizar_sueldo') is not null
drop procedure pa_empleados_actualizar_sueldo;

create procedure pa_empleados_actualizar_sueldo
@sueldoanterior decimal(10,2),
@sueldonuevo decimal(10,2)
as
begin
update empleados set sueldo = @sueldonuevo where sueldo = @sueldoanterior;
end;

exec pa_empleados_actualizar_sueldo 300, 350;

-- Ejercicio 5: Crear un procedimiento almacenado que reciba el documento de un empleado y muestre su nombre, apellido y el sueldo total.

if object_id('pa_sueldototal') is not null
drop procedure pa_sueldototal;

create procedure pa_sueldototal
@documento char(8) = '%'
as
begin
select nombre, apellido, sueldo + (case when sueldo < 500 then 200 else 100 end) * cantidadhijos as sueldototal
from empleados
where documento like @documento;
end;

exec pa_sueldototal '22333333';
exec pa_sueldototal '22444444';
exec pa_sueldototal '22666666';
exec pa_sueldototal;