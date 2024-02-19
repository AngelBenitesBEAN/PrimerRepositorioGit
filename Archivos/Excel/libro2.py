try:
    import pandas as pd

    # Definir la ruta al archivo Excel
    ruta = r'C:/Users/Usuario/Documents/Archivos/Libro1.xlsx'

    # Leer el archivo Excel y almacenar los datos en un DataFrame de Pandas
    df = pd.read_excel(ruta)

    # Imprimir los primeros 5 registros del DataFrame
    print("Primeros 5 registros del archivo Excel:")
    print(df.head())

except FileNotFoundError:
    print("El archivo no se encontró en la ruta especificada.")

except Exception as e:
    print("Ocurrió un error:", e)
