
#lista=[1,2,3,11,5,6,7,8,9]

#print("EL mayor es: ", max(lista))
    
#Escribir un programa que almacene las asignaturas de 
# un curso (por ejemplo Matemáticas, Física, Química, 
# Historia y Lengua) 
# en una lista y la muestre por pantalla.

lst=[]
asig=input("Ingrese el nombre de la asignatura: ")
lst.append(asig)
print(lst)
i=0
while i<1:
    seguir=input("Desea agregar otra asignatura? : ")
    if seguir=="si":
        asig=input("Ingrese el nombre de la asignatura: ")
        lst.append(asig)
        print(lst)
    else:
        print("Las asignaturas agregadas son: ", lst, "\n Gracias")
        break
#Gracias



