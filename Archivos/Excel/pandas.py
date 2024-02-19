import pandas as pd

libro=r'C:/Users/Usuario/Documents/Archivos/Libro1.xlsx'

try:
    df=pd.read_excel(libro)

    print(df.head())

except: 
    print("Error")