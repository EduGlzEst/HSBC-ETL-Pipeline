import yfinance as yf
import pandas as pd
import urllib.parse
from sqlalchemy import create_engine

# 1. EXTRACCIÓN: Descargar datos de yfinance
# HSBC Holdings plc cotiza como 'HSBC' en la bolsa de Nueva York
hsbc_stock = yf.Ticker("HSBC")
datos = hsbc_stock.history(period="1y", interval="1d")

# Limpieza: yfinance pone la Fecha como 'índice'. Lo pasamos a columna normal.
datos = datos.reset_index()
print("Primeras filas del historial de HSBC:")
print(datos.head())

# 2. CONEXIÓN: Preparar el puente a MySQL
mi_password_real = "TuNuevaContraseña123" # Cambia esto por tu contraseña local
password_codificada = urllib.parse.quote_plus(mi_password_real)
engine = create_engine(f"mysql+mysqlconnector://root:{password_codificada}@localhost:3306/hsbc")

# 3. CARGA: Enviar los datos a la base de datos
try:
    datos.to_sql(
        name='precios_hsbc_diarios', 
        con=engine, 
        if_exists='replace', 
        index=False
    )
    print("==========================")
    print("¡ÉXITO: Datos transferidos a MySQL!")
    print("Tabla: precios_hsbc_diarios")
    print("==========================")
except Exception as e:
    print("==========================")
    print(f"ERROR al transferir los datos: {e}")
    print("==========================")
