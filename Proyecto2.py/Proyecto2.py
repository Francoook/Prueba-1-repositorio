# Crear un programa para identificar la longitud de una palabra ingresada. 
# La palabra correcta debe tener entre cuatro y ocho letras. 
# toma en cuenta las siguientes consideraciones:
# Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, 
# se debe imprimir un mensaje que indique que la palabra es correcta
# Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: Hacen falta letras. 
# Solo tiene N letras (siendo N el número de letras de la palabra)
# Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. 
# Tiene N letras ((siendo N el número de letras de la palabra))



print("Bienvenido , el siguiente programa contará cuantas letras tiene la palabra que ingrese ")
palabra= input("Ingrese una palabra de 4 a 8 letras: ")

letras= len(palabra)
if 4 <= letras <= 8:
    print("Cantidad de letras correcta")
elif letras<4:
    diferencia= 4 - letras
    print(f"Hacen falta {diferencia} letra(s). Solo tiene {letras} letras")
elif letras> 8:
    diferencia = letras - 8
    print(f"Sobran letras {diferencia} letra(s). Tiene {letras} letras ")


print(f"la palabra {palabra} tiene {letras} letras")


# Crear un programa que en base a 2 números de entrada, coordenadas, 
# identifique en cuál de los 4 cuadrantes se encuentra el punto. 
# El programa debe verificar que ninguna coordenada sea 0. Por ejemplo

#Ingrese X: 4
#Ingrese Y: -5
#El punto se encuentra en el cuadrante IV.

#(X,Y): (+,+) => Cuad. I; (-,+) => Cuad. II; (-,-) => Cuad. III; (+,-) => Cuad. IV  

print("El siguiente programa, identificara en que cuadrante se encuentran las coordenadas X, Y")

x= int(input("Ingrese las coordernadas X: " ))
y= int(input('Ingrese la coordenada Y: '))
if x>0 and y>0:
    print("El punto se encuentra en el cuadrante I.")
elif x<0 and y>0:
    print("El punto se encuentra en el cuadrante II.")
elif x<0 and y<0:
    print("El punto se encuentra en el cuadrante III.")
elif x>0 and y<0:
    print("El punto se encuentra en el cuadrante IV.")



#




