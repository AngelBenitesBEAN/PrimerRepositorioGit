#Escribir un programa que almacene la cadena
# de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta 
# que introduzca la contraseña correcta.


contraseña=input("Ingrese una contraseña nueva: ")
print("\nContraseña registrada correctamente")


i=0

while i<1:
    registro=input("\nVerificacion, escriba su contraseña nuevamente: ")
    
    if (registro==contraseña):
        print("\nVerificacion realizada, contraseña correcta")
        break
    else: 
        print("\nContraseña incorrecta intente nuevamente")