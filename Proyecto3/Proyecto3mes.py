
import numpy as np 
import random
import matplotlib.pyplot as plt
ctidad_de_canicas= 3000
pruebas= 12
lista_de_canicas1=[]


for i in range (ctidad_de_canicas):
    casilla_donde_cae=0
    for canica in range (pruebas+1):
        resultado= random.randint(0,1)
        if resultado== 1:
            casilla_donde_cae +=1
    lista_de_canicas1.append(casilla_donde_cae)
     

plt.hist(lista_de_canicas1)
plt.title("Galton")
plt.ylabel("Cantidadde Canicas")
plt.xlabel("Casillero de las canicas")
plt.show()





#HISTOGRAMA 
# import numpy as np
# import matplotlib.pyplot as plt

# #datos= np.random.normal(media_distribucion, desviacion_estandar, tamano_muestra)

# datos= np.random.normal(0, 1.0, 3000)

# plt.hist(datos)
# plt.show()



#GRAFICO DE DISPERSION ES DECIR PUNTITOS

# import random 
# import matplotlib.pyplot as plt    

# eje_x= [random.randint(1,20) for n in range(10)]
# eje_y=  [random.randint(1,20) for n in range(10)]

# plt.scatter(eje_x,eje_y)
# plt.show()

#Proyectos13 GALTON

# Será la simulación de una máquina de Galton de 3000 canicas. 
# En total tendrá 12 niveles de obstáculos -deberás decidir si va a caer a un lado o al otro 12 veces.
# El resultado final será un histograma que represente la cantidad de canicas en cada contenedor, como el siguiente -No olvides colocar nombre a los ejes y un título al gráfico. 
# Deberás emplear dos funciones, una para calcular los resultados de las canicas y la segunda para la graficación del histograma.

# import numpy as np 
# import random
# import matplotlib.pyplot as plt

# canicas= 
# pruebas= 12
# lista_de_canicas=[]

# for i in canicas :
#     canica(0)
#     for j in pruebas:
#         decision= random.randint(1,2)
#         if decision == 1:
#             canica +=1
#         else:
#             canica+=0 

# datos= np.random.normal(1, 1, 3000)


# plt.hist(datos)
# plt.show()
 




