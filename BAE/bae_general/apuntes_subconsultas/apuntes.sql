
Ejercicio: Usar una Subconsulta
Enunciado: Queremos encontrar los nombres de los empleados que trabajan en el departamento con el mayor número de empleados.

3 - Escribir la subconsulta
La subconsulta nos ayudará a encontrar el DepartamentoID del departamento con más empleados. 
Luego, usaremos ese resultado en la consulta principal para obtener los nombres de los empleados.

-- subconsulta

SELECT DepartamentoID
FROM Empleados
GROUP BY DepartamentoID
ORDER BY COUNT(*) DESC
LIMIT 1;

2 - Integrar la subconsulta en la consulta principal
Ahora, usamos el resultado de la subconsulta para filtrar los empleados que pertenecen a ese departamento.

-- consulta principal

SELECT Nombre, Apellido
FROM Empleados
WHERE DepartamentoID = (
    SELECT DepartamentoID
    FROM Empleados
    GROUP BY DepartamentoID
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

Ejercicio adicional:

Subconsultas
Encuentra los nombres de los empleados que ganan más que el salario promedio de su departamento.

SELECT Nombre, Apellido
FROM Empleados e
WHERE Salario > (
    SELECT AVG(Salario)
    FROM Empleados
    WHERE DepartamentoID = e.DepartamentoID
);

