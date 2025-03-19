if object_id('proc_contador','P') is not null
drop procedure proc_contador;
go
create procedure proc_contador
as
DECLARE @contador int;
SET @contador = 1;
WHILE (@contador <= 20)
BEGIN
PRINT 'Iteracion del bucle '
+ cast(@contador AS varchar);
SET @contador = @contador + 1;
END
print 'Final';
go
exec proc_contador;