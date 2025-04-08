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






---------------------------------------------------------------------------------------------------------
IF object_id('CrearRestriccion') IS NOT NULL
DROP procedure [CrearRestriccion]
go
create procedure CrearRestriccion
as
declare @sentencia varchar(1000)
declare @Tabla varchar(100)
declare CUR cursor for
select Tabla
from ciclismo.dbo.datostablas;
open CUR

fetch next from CUR
into @Tabla
while @@FETCH_STATUS=0
begin
set @sentencia='alter table '+@tabla+
' drop CONSTRAINT U_'+@tabla
-- print @sentencia
begin try
exec(@sentencia)
end try
begin catch
print 'Índice no existe: U_'+@tabla
end catch
set @sentencia='alter table '+@tabla+
' add CONSTRAINT U_'+@tabla
set @sentencia+=' unique(' + @Tabla +'); '
exec (@sentencia)
-- print @sentencia
fetch next from CUR
into @Tabla
end
close cur
deallocate cur
print'OK'
go