if object_id('proc_contador','P') is not null
drop procedure proc_contador;
go
create procedure proc_contador
as
DECLARE @cadena nvarchar(50);
DECLARE @contador int;
SET @cadena = 'Hola Mundo';
SET @contador = 1;
WHILE (@contador <= LEN(@cadena))
BEGIN
PRINT 'Caracter en la posicion ' + cast(@contador AS varchar) + ': ' + SUBSTRING(@cadena, @contador, 1);
SET @contador = @contador + 1;
END
print 'Final';
go
exec proc_contador;