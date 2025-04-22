
	 	 	 	
-- Partiendo de las siguientes tablas que se encuentra en una nueva base de datos.
Create table Ventas (
	id int identity,
	cod char(5),
	mes char(2),
	importe decimal(8,2)
	)
	
create table meses(
	cod char(2) PRIMARY KEY,
	nombre varchar(10)
	)	
INSERT INTO VENTAS VALUES ('00001', '01',100),
('00001', '02',200),
('00001', '03',250),
('00001', '04',100),
('00001', '05',150),
('00001', '06',100),
('00002', '01',150),
('00002', '02',150),
('00002', '03',150),
('00002', '04',100),
('00002', '05',100),
('00002', '06',100)



INSERT INTO MESES VALUES ('01', 'Enero'),
('02', 'Febrero'),
('03', 'Marzo'),
('04', 'Abril'),
('05', 'Mayo'),
('06', 'Junio')



-- Donde se almacenan en ventas, las ventas realizadas por un vendedor (cod), en un mes determinado (mes) y con un importe (importe).

-- Se pide realizar un procedimiento almacenado que contenga un cursor y que muestre las ventas acumuladas de un determinado vendedor, algo parecido a lo que se muestra a continuación: (en este caso para el vendedor de cod = 2)


CREATE PROCEDURE sp_VentasAcumuladas
    @cod char(5)
AS
BEGIN
    DECLARE @importe decimal(8,2), @acumulado decimal(8,2), @mes char(2)
    DECLARE cur_Ventas CURSOR FOR
        SELECT mes, importe
        FROM Ventas
        WHERE cod = @cod
        ORDER BY mes

    OPEN cur_Ventas

    FETCH NEXT FROM cur_Ventas INTO @mes, @importe

    SET @acumulado = 0

    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @acumulado = @acumulado + @importe
        PRINT 'Mes: ' + @mes + ', Importe: ' + CONVERT(varchar, @importe) + ', Acumulado: ' + CONVERT(varchar, @acumulado)
        FETCH NEXT FROM cur_Ventas INTO @mes, @importe
    END

    CLOSE cur_Ventas
    DEALLOCATE cur_Ventas
END