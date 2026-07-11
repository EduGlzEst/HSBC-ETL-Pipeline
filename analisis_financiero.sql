-- 1. Agregar columnas para el análisis de riesgo y temporalidad
ALTER TABLE hsbc.precios_hsbc_diarios
ADD COLUMN Spread FLOAT,
ADD COLUMN anio INT,
ADD COLUMN mes INT;

-- 2. Calcular la volatilidad diaria (Spread) y extraer datos de fecha
UPDATE hsbc.precios_hsbc_diarios
SET 
    Spread = High - Low,
    anio = YEAR(`Date`),
    mes = MONTH(`Date`);

-- 3. Análisis: Obtener el rendimiento promedio por mes (Ordenado de mayor a menor)
SELECT mes as MES, AVG(Close) AS Rendimiento_promedio
FROM hsbc.precios_hsbc_diarios
GROUP BY mes 
ORDER BY Rendimiento_promedio DESC;