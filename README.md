# 🏦 Financial ETL Pipeline: Stock Market Data to MySQL

## 📊 Business Overview
Este proyecto automatiza el flujo de datos (ETL) de la información bursátil de HSBC Holdings plc. El objetivo es extraer el historial de precios desde Yahoo Finance, estructurar los datos y almacenarlos en una base de datos relacional (MySQL) para su posterior análisis financiero.

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python, SQL
* **Librerías Python:** `yfinance` (Extracción), `pandas` (Transformación), `sqlalchemy` (Carga)
* **Base de Datos:** MySQL

## ⚙️ Arquitectura del Pipeline
1. **Extract (Extracción):** Consumo de datos bursátiles mediante `yfinance` para descargar el historial diario de precios de las acciones de HSBC correspondientes al último año.
2. **Transform (Transformación):** Limpieza y formateo de los datos utilizando `pandas`, preparando la estructura para un entorno relacional.
3. **Load (Carga):** Conexión segura a la base de datos MySQL utilizando `sqlalchemy` y transferencia del DataFrame a la tabla `precios_hsbc_diarios`.

## 📈 Análisis Financiero (SQL)
Una vez que los datos están disponibles en el motor de base de datos, se ejecutan rutinas analíticas en SQL:
* **Cálculo de Volatilidad (Spread):** Diferencia calculada entre los precios máximos (*High*) y mínimos (*Low*) intradía.
* **Rendimientos Mensuales:** Agrupación y cálculo del precio de cierre promedio mensual (*Average Close Price*) para identificar tendencias de rendimiento.

## 🚀 Cómo ejecutar este proyecto
1. Clona el repositorio.
2. Instala las dependencias: `pip install pandas yfinance sqlalchemy mysql-connector-python`
3. Ajusta las credenciales de tu servidor MySQL local en el script de Python.
4. Ejecuta `hsbc_etl_pipeline.py`.
5. Ejecuta las consultas de `analisis_financiero.sql` en tu gestor de base de datos.
