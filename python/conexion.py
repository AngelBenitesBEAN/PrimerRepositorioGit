import pyodbc

server = 'nombre_del_servidor'
database = 'nombre_de_la_base_de_datos'
username = 'nombre_de_usuario'
password = 'contraseña'

connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'


try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Conexión exitosa")
except Exception as e:
    print("Error al conectar a la base de datos:", e)
    
try:
    cursor.execute("SELECT * FROM NombreDeTabla")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print("Error al ejecutar la consulta:", e)
    
conn.close()