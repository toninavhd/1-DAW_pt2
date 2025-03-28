if object_id('pa_seccion') is not null
drop procedure pa_seccion;
go
-- 4- Cree un procedimiento almacenado llamado "pa_seccion" al cual le enviamos el nombre de una sección y que nos retorne en un parámetro de salida el promedio de sueldos de todos los empleados de esa sección y el valor mayor de sueldo (de esa sección).

create procedure pa_seccion
@seccion varchar(20) = null,
@promedio decimal(6,2) output,
@mayor decimal(6,2) output
as
begin
    if @seccion is null
        select @promedio = avg(sueldo), @mayor = max(sueldo)
        from empleados
    else
        select @promedio = avg(sueldo), @mayor = max(sueldo)
        from empleados
        where seccion = @seccion
end
go

-- 5- Llame al procedimiento almacenado "pa_seccion"
declare @promedio decimal(6,2), @mayor decimal(6,2)
exec pa_seccion 'Contaduria', @promedio output, @mayor output
print 'Promedio: ' + convert(varchar, @promedio) + ', Mayor: ' + convert(varchar, @mayor)
go

declare @promedio decimal(6,2), @mayor decimal(6,2)
exec pa_seccion null, @promedio output, @mayor output
print 'Promedio: ' + convert(varchar, @promedio) + ', Mayor: ' + convert(varchar, @mayor)
go

if object_id('pa_sueldototal') is not null
drop procedure pa_sueldototal;
go

-- 6- Cree un procedimiento almacenado llamado "pa_sueldototal"

create procedure pa_sueldototal
@documento char(8),
@sueldototal decimal(6,2) output
as
begin
    declare @sueldo decimal(6,2), @cantidadhijos tinyint
    select @sueldo = sueldo, @cantidadhijos = cantidadhijos
    from empleados
    where documento = @documento

    if @sueldo is null
        set @sueldototal = null
    else if @sueldo < 500
        set @sueldototal = @sueldo + (@cantidadhijos * 200)
    else
        set @sueldototal = @sueldo + (@cantidadhijos * 100)
end
go

-- 7- Llame al procedimiento almacenado "pa_sueldototal"

declare @sueldototal decimal(6,2)
exec pa_sueldototal '22222222', @sueldototal output
print 'Sueldo total: ' + convert(varchar, @sueldototal)
go

declare @sueldototal decimal(6,2)
exec pa_sueldototal '12345678', @sueldototal output
print 'Sueldo total: ' + convert(varchar, @sueldototal)
go

declare @sueldototal decimal(6,2)
exec pa_sueldototal '22555555', @sueldototal output
print 'Sueldo total: ' + convert(varchar, @sueldototal)
go