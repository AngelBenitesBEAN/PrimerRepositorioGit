import mysql.connector
import pywhatkit

conexion = mysql.connector.connect(host="localhost",user="root",password="",database="practicas")

cursor= conexion.cursor()

cursor.execute("SELECT name FROM datos Where estado='N'")

res= cursor.fetchall()
lista=[]
for i in res:
    mensaje=f"Los clientes {i} aun no reciben su pedido, realiza un seguimiento"

pywhatkit.sendwhatmsg("+51922304900",mensaje,22,31,15,True,5)

cursor.close()
conexion.close()
