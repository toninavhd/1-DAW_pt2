USE audienciasbasicas
GO
-- Suma de audiencia de programas para cada cadena en martes y para las cadenas con tres o menos programas.

SELECT cadena, SUM(Espectadores) AS total_audiencia
FROM Datosprogramas
WHERE DATENAME(dw, FechaHora) = 'Martes'
GROUP BY cadena
HAVING COUNT(programa) <= 3;

-- Mostrar las cadenas con media de share mayor que 10 en el horario de las 10, 11 y 12 de la mañana.

SELECT cadena
FROM Datosprogramas
WHERE DATEPART (HOUR,FechaHora) BETWEEN 10 and 12
GROUP BY cadena
HAVING AVG(share) > 10;

