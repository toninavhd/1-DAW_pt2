alter table factura
add constraint FK_facturatienda
foreign key (idTienda)
references Tienda (idTienda);
go

alter table facturacomponente
add constraint FK_facturacomponente1
foreign key (Nfactura)
references Factura (NFactura);
go

alter table facturacomponente
add constraint FK_facturacomponente2
foreign key (CodComponente)
references Componente (clave);
go

alter table componente
add constraint FK_componentetipo
foreign key (CodTipo)
references TipoComponente (CodTipo);
go


/*1.- Crear Procedimiento almacenado al que le pasemos como parámetro el nombre del
Mes, que valide si es correcto y que devuelva en un parámetro de salida el nº de
facturas del mes indicado y un -1 si el nombre del mes es incorrecto. Dar tres ejemplos
de prueba*/

CREATE PROCEDURE spFacturasMes
    @Mes nvarchar(20),
    @TotalFacturas int Output,
    @Error int Output

AS
BEGIN
    DECLARE @TypeId int = NULL
    DECLARE @Fecha datetime

    SET @Fecha = convert(date, YEAR(GETDATE()) * 100 + MONTH(@Fecha))

    SELECT @TypeId = 
    CASE @Mes
        WHEN 'Enero' THEN 1
        WHEN 'Febrero' THEN 2
        WHEN 'Marzo' THEN 3
        WHEN 'Abril' THEN 4
        WHEN 'Mayo' THEN 5
        WHEN 'Junio' THEN 6
        WHEN 'Julio' THEN 7
        WHEN 'Agosto' THEN 8
        WHEN 'Septiembre' THEN 9
        WHEN 'Octubre' THEN 10
        WHEN 'Noviembre' THEN 11
        WHEN 'Diciembre' THEN 12
        ELSE NULL
    END

    IF @TypeId IS NULL
    BEGIN
        SET @Error = -1
        PRINT 'Error: El mes ' + @Mes + ' es incorrecto.'
    END
    ELSE
    BEGIN
        SELECT @TotalFacturas = COUNT(*)
              FROM Factura
              WHERE MONTH(Fecha) = @TypeId AND YEAR(Fecha) = YEAR(GETDATE())

        IF @TotalFacturas = 0
        BEGIN
            SET @Error = -1
            PRINT 'Error: No hay facturas para el mes ' + @Mes
        END
    END
END
GO

-- Ejemplos de ejecución
DECLARE @TotalFacturas int
DECLARE @Error int

EXEC spFacturasMes 'Enero', @TotalFacturas Output, @Error Output
PRINT 'Total facturas: ' + convert(nvarchar(10), @TotalFacturas)

EXEC spFacturasMes 'Diciembre', @TotalFacturas Output, @Error Output
PRINT 'Total facturas: ' + convert(nvarchar(10), @TotalFacturas)

EXEC spFacturasMes 'EneroXXXX', @TotalFacturas Output, @Error Output
PRINT 'Total facturas: ' + convert(nvarchar(10), @TotalFacturas)
GO

/*2.- Hacer un procedimiento almacenado que muestre el día de los N próximos meses a
partir de la fecha de hoy, con N entrado como parámetro, con valor por defecto 10.
Si hoy es 8/6/2013, para N=8 deberá salir en formato fecha:
Jul 8 2013 11:10AM
Ago 8 2013 11:10AM
Sep 8 2013 11:10AM
Oct 8 2013 11:10AM
Nov 8 2013 11:10AM
Dic 8 2013 11:10AM
Ene 8 2014 11:10AM
Feb 8 2014 11:10AM*/

CREATE PROCEDURE spFechaN    
    @N int = 10  
AS    
BEGIN    
    DECLARE @FechaActual datetime = getdate();   
    DECLARE @nMes int = DATEPART(month, GETDATE())+ @N;    
    DECLARE @nAno int = YEAR(GETDATE());    
        
    WHILE (DATEPART(month, @FechaActual) <= @nMes OR (DATEPART(month, @FechaActual) <=2 AND @nMes <= 2)) AND @N > 0  ;     
    BEGIN   
        SET @FechaActual = dateadd(day, 1, @FechaActual);    
        SET @N = @N -1;    
    END;    
        
    WHILE (DATEPART(month, @FechaActual) > @nMes OR  (DATEPART(month, @FechaActual) >2 AND @nMes <= 2))       
    BEGIN   
        SET @FechaActual = dateadd(day, -1, @FechaActual);    
    END;    
        
    SELECT
        DATENAME(month, dateadd(month, 0, @FechaActual))+
        ' '+ 
        DAY(dateadd(month, 0, @FechaActual))+
        ' ' + 
        YEAR(dateadd(year, 0, @FechaActual))+
        ' 11:10AM'
        
    WHILE (@N) > 0    
    BEGIN    
        IF DATEPART(month, @FechaActual) > 12
        BEGIN 
            SET @FechaActual = dateadd(month, -12, @FechaActual);  
        END       
        ELSE 
        BEGIN
            SET @FechaActual = dateadd(month, -1, @FechaActual);   
        END      
        SELECT
            DATENAME(month, dateadd(month, 0, @FechaActual))+
            ' '+ 
            DAY(dateadd(month, 0, @FechaActual))+
            ' ' + 
            YEAR(dateadd(year, 0, @FechaActual))+
            ' 11:10AM'   
        SET @N = @N-1;
    END;
END;   
GO

EXEC spFechaN

/*3.- Crear Procedimiento almacenado que actualice la tabla componente, aplicándole
un 5% de incremento a los precios de los componentes de un CodTipo pasado como
parámetro. Validará que hay componentes del tipo pasado, mostrando un mensaje en
el caso de que no existan y el número de componentes modificados en el caso de que
sí existan.
*/

CREATE PROCEDURE spActualizarComponente
    @CodTipo int
AS
BEGIN
    DECLARE @NumComponentes int

    SELECT @NumComponentes = COUNT(*)
    FROM Componente
    WHERE CodTipo = @CodTipo

    IF @NumComponentes = 0
    BEGIN
        PRINT 'No hay componentes del tipo ' + CONVERT(nvarchar(10), @CodTipo)
    END
    ELSE
    BEGIN
        UPDATE Componente
        SET precio = precio * 1.05
        WHERE CodTipo = @CodTipo

        PRINT 'Se han actualizado ' + CONVERT(nvarchar(10), @NumComponentes) + ' componentes del tipo ' + CONVERT(nvarchar(10), @CodTipo)
    END
END
GO

/*
4.- Crear un procedimiento almacenado que le pasemos como parámetro un texto y
que devuelva en un parámetro de salida los símbolos que no sean las vocales (con o
sin acento).
Hacer un ejemplo de ejecución.
*/

CREATE PROCEDURE spDevuelveSimbolosSinVocales    
    @texto nvarchar(50),    
    @textoSinVocales nvarchar(50) OUTPUT    
AS    
BEGIN    
    DECLARE @i int = 1;    
    DECLARE @longitud int = LEN(@texto);    
        
    WHILE @i <= @longitud    
    BEGIN    
        DECLARE @letra nvarchar(1) = SUBSTRING(@texto, @i, 1);    
            
        IF LOWER(@letra) NOT IN ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')    
        BEGIN    
            SET @textoSinVocales = @textoSinVocales + @letra;    
        END    
        SET @i = @i + 1;    
    END;    
END;    
GO    

-- Ejemplo de ejecución
DECLARE @texto nvarchar(50) = 'Hello World áéíóú';
DECLARE @textoSinVocales nvarchar(50);
EXEC spDevuelveSimbolosSinVocales @texto, @textoSinVocales OUTPUT;
PRINT @textoSinVocales;

CREATE PROCEDURE spBuscarComponente    
    @descripcion nvarchar(100),    
    @numComponentes int OUTPUT    
AS    
BEGIN    
    SELECT @numComponentes = COUNT(*)    
    FROM Componente    
    WHERE descripcion LIKE '%' + @descripcion + '%';    
END    
GO    

-- Ejemplo de ejecución
DECLARE @descripcion nvarchar(100) = 'Intel';
DECLARE @numComponentes int;
EXEC spBuscarComponente @descripcion, @numComponentes OUTPUT;
PRINT @numComponentes

/*
5.- Crear procedimiento almacenado que le pasemos un texto como parámetro y
devuelva en un parámetro de salida el nº de componentes cuya descripción contenga el
texto suministrado. Hacer un ejemplo de ejecución.
*/

CREATE PROCEDURE spBuscarComponente    
    @descripcion nvarchar(100),    
    @numComponentes int OUTPUT    
AS    
BEGIN    
    SELECT @numComponentes = COUNT(*)    
    FROM Componente    
    WHERE descripcion LIKE '%' + @descripcion + '%';    
END    
GO    

-- Ejemplo de ejecución
DECLARE @descripcion nvarchar(100) = 'Intel';
DECLARE @numComponentes int;
EXEC spBuscarComponente @descripcion, @numComponentes OUTPUT;
PRINT @numComponentes
GO


