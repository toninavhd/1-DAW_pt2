SELECT DISTINCT CA FROM DatosCompletosTabla WHERE CA LIKE '%ia%'

SELECT DISTINCT CA FROM DatosCompletosTabla WHERE CA LIKE '[aeiouáéíóú]%'

SELECT COUNT(DISTINCT Provincia) FROM DatosCompletosTabla WHERE CA = 'Canarias' 

SELECT SUM(Padron) FROM DatosCompletosTabla WHERE CA = 'Canarias'