Ejercicios vistas:
 -- 1. Probar una consulta que nos muestre el total de parados por provincia para el mes de enero. Sacará también el nombre de la Comunidad autónoma.
SELECT p.Provincia, ca.CA, SUM(pm.TotalParoRegistrado) AS TotalParo
FROM Provincias p
INNER JOIN ComunidadesAutonomas ca ON p.CodCA = ca.CodCA
INNER JOIN ParoMes pm ON p.CodProvincia = pm.CodMunicipio
WHERE MONTH(pm.Fecha) = 1
GROUP BY p.Provincia, ca.CA;

-- 2. Crear una vista basada en esa consulta. (ver_paro_provincia)
CREATE VIEW ver_paro_provincia AS
SELECT p.Provincia, ca.CA, SUM(pm.TotalParoRegistrado) AS TotalParo
FROM Provincias AS p
INNER JOIN ComunidadesAutonomas ca ON p.CodCA = ca.CodCA
INNER JOIN ParoMes pm ON p.CodProvincia = pm.CodMunicipio
WHERE MONTH(pm.Fecha) = 1
GROUP BY p.Provincia, ca.CA;

-- 3. Usar la vista sacando todos sus datos.
SELECT * FROM ver_paro_provincia;
-- 4. Usar la vista para sacar la suma de parados por Comunidad Autónoma.
SELECT CA, SUM(TotalParo) AS TotalParo
FROM ver_paro_provincia
GROUP BY CA;

-- 5. Crear una vista sobre la tabla ComunidadesAutonomas
CREATE VIEW ver_comunidades AS
SELECT * FROM ComunidadesAutonomas;

-- 6. Ver los datos que contiene
SELECT * FROM ver_comunidades;

-- 7. Borrar la vista anterior comprobando que existe
IF OBJECT_ID('ver_comunidades', 'V') IS NOT NULL
DROP VIEW ver_comunidades;

-- 8. Mostrar la estructura de la vista ver_paro_provincia

EXEC sp_helptext 'ver_paro_provincia';

-- 9. Crear de nuevo la vista pero encriptada

CREATE VIEW ver_paro_provincia_encriptada
WITH ENCRYPTION
AS
SELECT p.Provincia, ca.CA, SUM(pm.TotalParoRegistrado) AS TotalParo
FROM Provincias p
JOIN ComunidadesAutonomas ca ON p.CodCA = ca.CodCA
JOIN ParoMes pm ON p.CodProvincia = pm.CodMunicipio
WHERE MONTH(pm.Fecha) = 1
GROUP BY p.Provincia, ca.CA;

-- 10. Comprobar que no se puede ver su estructura

EXEC sp_helptext 'ver_paro_provincia_encriptada';

-- 11. Actualizar el nombre de una Comunidad Autónoma a través de la vista

UPDATE ComunidadesAutonomas
SET CA = 'Nuevo Nombre'
WHERE CodCA = 1;

-- 12. Intentar una inserción

INSERT INTO ComunidadesAutonomas (CodCA, CA)
VALUES (20, 'Nueva Comunidad');

-- 13. Crear una vista que acceda a las Comunidades autónomas solamente

CREATE VIEW ver_comunidades_autonomas AS
SELECT * FROM ComunidadesAutonomas;

-- 14. Hacer una inserción correcta sobre esa vista

INSERT INTO ver_comunidades_autonomas (CodCA, CA)
VALUES (20, 'Nueva Comunidad');

-- 15. Borrar el registro creado anteriormente, usando también la vista

DELETE FROM ver_comunidades_autonomas
WHERE CodCA = 20;

-- 16. Crear una vista que muestre sólo las Comunidades autónomas que comiencen con C y con la opción with check option

CREATE VIEW ver_comunidades_con_C
AS
SELECT * FROM ComunidadesAutonomas
WHERE CA LIKE 'C%'
WITH CHECK OPTION;

-- 17. Probar inserciones y modificaciones que validen el funcionamiento de la opción aplicada

-- Inserción válida
INSERT INTO ComunidadesAutonomas (CodCA, CA)
VALUES (21, 'Cantabria');

-- Inserción inválida
INSERT INTO ComunidadesAutonomas (CodCA, CA)
VALUES (22, 'Andalucía');

-- Modificación válida
UPDATE ComunidadesAutonomas
SET CA = 'Castilla y León'
WHERE CodCA = 7;

-- Modificación inválida
UPDATE ComunidadesAutonomas
SET CA = 'Madrid, Comunidad de'
WHERE CodCA = 13;

-- 18. Modificar la vista anterior filtrando a comunidades autónomas que comiencen por 

CREATE VIEW ver_comunidades_con_A
AS
SELECT * FROM ComunidadesAutonomas
WHERE CA LIKE 'A%'
WITH CHECK OPTION;