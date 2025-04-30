USE parobasicas

SELECT DISTINCT CA FROM DatosCompletosTabla WHERE CA LIKE '[aeiouáéíóú]%'

SELECT SUM(Padron) as poblacion , COUNT(TotalParoRegistrado) as TasaParo FROM DatosCompletosTabla WHERE Fecha ='01/03/2013' AND ISLA IS NOT NULL GROUP BY ISLA

SELECT TOP 3  Municipio, AVG(TotalParoRegistrado) AS mediaparo FROM DatosCompletosTabla WHERE CA = 'Canarias' GROUP BY Municipio ORDER BY mediaparo DESC

SELECT 
    provincia,
    CA,
    COUNT(municipio) AS municipios_con_paro_alto
FROM 
    DatosCompletosTabla
WHERE 
    Fecha='1/1/2013' AND TotalParoRegistrado > (Padron * 0.2)
GROUP BY 
    provincia, CA
ORDER BY 
    CA 