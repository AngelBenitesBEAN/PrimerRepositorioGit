import mysql.connector
import pywhatkit

conexion = mysql.connector.connect(host="localhost",user="root",password="",database="practicas")

cursor= conexion.cursor()

cursor.execute("SELECT name FROM datos Where estado='N'")

res= cursor.fetchall()
lista=[]
for i in res:
    lista.append(i[0])

lista_nueva=lista
nombre_usu=""
for nombre in lista_nueva:
    nombre_usu += nombre + ", "

mensaje = f"Los clientes {nombre_usu} aun no reciben "

pywhatkit.sendwhatmsg("+51973196845",mensaje,12,2,10,True,3)

cursor.close()
conexion.close()