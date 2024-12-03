USE parobasicas
GO
----
SELECT ca, SUM(padron) AS total_padron
FROM DatosCompletosTabla
WHERE fecha = '1/3/2013'
GROUP BY CA
HAVING COUNT(provincia)>5


SELECT SUM(TotalParoRegistrado) AS total_paro
FROM DatosCompletosTabla
WHERE fecha = ' 1/1/2013'
GROUP BY provincia
HAVING COUNT(isla) = 4

----