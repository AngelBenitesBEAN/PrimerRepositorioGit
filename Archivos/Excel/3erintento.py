import pandas as pd

df_modelo= pd.ExcelFile('C:\Users\Usuario\Documents\Archivos\Libro1.xlsx').parse(sheet_name='modelo',header=0,
                            names=None,index_col=None, encoding= 'laint-1')

df_modelo.head()
                                                                