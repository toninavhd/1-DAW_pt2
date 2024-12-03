USE audienciasbasicas
GO

SELECT cadena, SUM(Espectadores) AS total_audiencia
FROM Datosprogramas
WHERE DATENAME( FechaHora , 2) = 'martes'
GROUP BY cadena
HAVING COUNT(programa) <= 3;

SELECT cadena
FROM Datosprogramas
WHERE FechaHora IN ('10:00:00', '11:00:00', '12:00:00')
GROUP BY cadena
HAVING AVG(share) > 10;

