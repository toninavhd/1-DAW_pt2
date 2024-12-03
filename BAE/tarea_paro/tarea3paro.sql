USE parobasicas
GO

-- Sumar el padrón de las ca con más de 5 provincias para datos del 1/3/2013
SELECT ca, SUM(padron) AS total_padron
FROM DatosCompletosTabla
WHERE fecha = '1/3/2013'
GROUP BY CA
HAVING COUNT(provincia)>5

-- Sumar el paro de las provincias con 4 islas (usando having) para datos 1/1/2013.
SELECT SUM(TotalParoRegistrado) AS total_paro
FROM DatosCompletosTabla
WHERE fecha = ' 1/1/2013'
GROUP BY provincia
HAVING COUNT(isla) > 4
