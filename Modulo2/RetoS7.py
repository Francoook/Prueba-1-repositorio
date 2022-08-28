#Programa creara una lista que capturara el nombre 
# y dos calificaciones, de hasta 5 alumnos en un ciclo que 
# termine cuando se cumpla cierta condicion especifica, 
# al finalizar el ciclo se debe mostrar una lista 
# con los nombres de los alumnos 
# con su inicial con nombre en mayuscula y su respectivas calificaciones 


#from pickle import APPEND
#from readline import append_history_file


lista= []
qcalificaciones  = 0
qalumnos= 0

intentos = 0
while  qalumnos > 4:
    opcion = int(input("Agregar alumnos (1) o terminar programa (2):  "))
    if opcion == 1:
        1< qcalificaciones <= 3
        nombre = input(" Ingrese el nombre del alumno :  ").capitalize()
        calificacion1 = float(input(f"Ingrese la primera calificacion de {nombre} :  "))
        calificacion2 = float(input(f"Ingrese la segunda calificacion de {nombre}: "))
        calificaciones3 = float(input(f'Ingrese la tercera calificacion de {nombre}:  '))
        alumnos = [ nombre , calificacion1 , calificacion2  ]
        lista.append(alumnos)
        
        cantidadAlumnos +=1
    elif opcion == 2:
        break
    else:
        print("Se ha ingresado una opcion invalida")
        continue

print("La lista de alumnos es:")
print(lista)



