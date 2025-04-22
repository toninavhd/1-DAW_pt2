--Una librería almacena los datos de sus libros en una tabla
--denominada "libros" y en otra tabla llamada "ventas", las
--ventas de los mismos.
--Eliminamos las tablas si existen:
use pruebasql
go
if object_id('ventas') is not null
drop table ventas;
if object_id('libros') is not null
drop table libros;
go
--Creamos las tablas, con las siguientes estructuras:
create table libros(
codigo int,
titulo varchar(40),
autor varchar(30),
precio decimal(6,2),
stock int,
constraint PK_libros primary key(codigo)
);
create table ventas(
numero int,
fecha datetime,
codigolibro int not null,
precio decimal (6,2),
cantidad int,
constraint PK_ventas primary key(numero),
constraint FK_ventas_codigolibro
foreign key (codigolibro) references libros(codigo)
);
g