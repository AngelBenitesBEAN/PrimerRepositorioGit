

import pandas as pd

# Definir la ruta al archivo Excel
ruta = r'C:/Users/Usuario/Documents/Archivos/Libro1.xlsx'

try:
    # Intentar leer el archivo Excel
    df = pd.read_excel(ruta, header=None)

    # Imprimir los primeros 5 registros del DataFrame
    print(df.head())

except FileNotFoundError:
    print("El archivo no se encontró en la ruta especificada.")

except Exception as e:
    print("Ocurrió un error:", e)


