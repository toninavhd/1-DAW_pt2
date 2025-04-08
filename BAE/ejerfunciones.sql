--FUNCIÓN DE TABLA DE VARIAS INSTRUCCIONES
if object_id('f_Ver3IdMax') is not null
drop function f_Ver3IdMax;
go
CREATE FUNCTION dbo.f_Ver3IdMax()
returns @tablasalida table
(
tabla varchar(100),
idmax int
)
as
begin
insert @tablasalida
select top 3 'puntuacion',id
from puntuacion
order by id desc;
--
insert @tablasalida
select top 3 'cliente',id
from cliente
order by id desc;
--
insert @tablasalida
select top 3 'disco',iddisco
from disco
order by iddisco desc;
return
end
go
--
select tabla,idmax
from f_Ver3IdMax();
go


--HACER UNA MODIFICACIÓN A LA FUNCIÓN ANTERIOR.
--1- LE PASAREMOS EL NOMBRE DE UNA TABLA Y NOS DEVOLVERÁ EL RESULTADO DE ESA TABLA
--2- LE PASAREMOS EL NOMBRE DE UNA TABLA Y NOS DEVOLVERÁ EL RESULTADO DE ESA TABLA
-- Y SI LE PASAMOS TODAS NOS DEVUELVE EL RESULTADO DE TODAS

if object_id('f_Ver3IdMax') is not null
drop function f_Ver3IdMax;
go
CREATE FUNCTION dbo.f_Ver3IdMax
(
    @tabla varchar(100) = 'todas'
)
returns @tablasalida table
(
    tabla varchar(100),
    idmax int
)
as
begin
    if @tabla = 'todas'
    begin
        insert @tablasalida
        select top 3 'puntuacion',id
        from puntuacion
        order by id desc;
        --
        insert @tablasalida
        select top 3 'cliente',id
        from cliente
        order by id desc;
        --
        insert @tablasalida
        select top 3 'disco',iddisco
        from disco
        order by iddisco desc;
    end

    else if @tabla = 'puntuacion'
    begin
        insert @tablasalida
        select top 3 'puntuacion',id
        from puntuacion
        order by id desc;
    end
    else if @tabla = 'cliente'
    begin
        insert @tablasalida
        select top 3 'cliente',id
        from cliente
        order by id desc;
    end
    
    else if @tabla = 'disco'
    BEGIN
        insert @tablasalida
        select top 3 'disco',iddisco
        from disco
        order by iddisco desc;
    end
  
end
go
--
select tabla,idmax
from f_Ver3IdMax('todas');
go
--
select tabla,idmax
from f_Ver3IdMax('puntuacion');
go
--
select tabla,idmax
from f_Ver3IdMax('cliente');
go
--
select tabla,idmax
from f_Ver3IdMax('disco');
go