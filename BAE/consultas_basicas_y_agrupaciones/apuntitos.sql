SELECT DISTINCT CA FROM DatosCompletosTabla WHERE CA LIKE '%ia%'

SELECT DISTINCT CA FROM DatosCompletosTabla WHERE CA LIKE '[aeiouáéíóú]%'

SELECT COUNT(DISTINCT Provincia) FROM DatosCompletosTabla WHERE CA = 'Canarias' 

SELECT SUM(Padron) FROM DatosCompletosTabla WHERE CA = 'Canarias'

SELECT SUM(DISTINCT Padron) AS padron, COUNT(DISTINCT Municipio) AS Municip FROM DatosCompletosTabla WHERE Fecha = '01/01/2013'

SELECT COUNT(DISTINCT Municipio) FROM DatosCompletosTabla WHERE CA ='Canarias'

SELECT CA,SUM(Padron) FROM DatosCompletosTabla WHERE fecha ='01/01/2013' GROUP BY CA ORDER BY SUM(Padron) DESC

SELECT Provincia, AVG(TotalParoRegistrado) FROM DatosCompletosTabla GROUP BY Provincia

-- ESTE ES EL ORDEN PARA REALIZAR LAS CONSULTAS
SELECT CA, SUM(Padron) -- Lo que quieres buscar
FROM DatosCompletosTabla -- Tabla donde buscar
WHERE Fecha='01/01/2013' -- Donde lo quieres buscar
GROUP BY CA -- Por donde agruparlo
HAVING SUM(Padron)<2000000 -- Condiciones numericas
ORDER BY COUNT(*) DESC -- Ordenarlo por lo que necesites

SELECT DISTINCT Municipio FROM DatosCompletosTabla WHERE CA = 'Rioja, La' GROUP BY Municipio

SELECT DISTINCT Provincia FROM DatosCompletosTabla WHERE CA = 'Canarias' OR CA = 'Cantabria' OR CA = 'Galicia'


SELECT 
    provincia,
    CA,
    COUNT(municipio) AS municipios_con_paro_alto
FROM 
    DatosCompletosTabla
WHERE 
    TotalParoRegistrado > (Padron * 0.2)
GROUP BY 
    provincia, CA
ORDER BY 
    provincia, CA;

