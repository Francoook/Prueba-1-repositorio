#IMC PRUEBA 1 



personas = int(input( "Cantidad de personas: "))




nombre= input("Ingrese su nombre: ")
apellidoP= (input("Ingrese su apellido Paterno: "))
apellidoM= input("Ingrese su apellido Materno: ")

fedad= int(input("Ingrese su edad: "))
peso= float(input(("Ingrese su peso en kilogramos: ")))
estatura= float(input("Ingrese su estatura en metros :"))

estatura2= float(estatura**2)

imc= (float(peso/(estatura2)))

print ("Su indice de masa corporal es:  ", (str(imc)))

if imc >= 0 and  imc <= 15.99 :
    print ("Delgadez severa")
elif imc >= 16.00 and imc <= 16.99 :
    print("Delgadez moderada ")
elif imc >= 17.00 and imc <= 18.49 : 
    print("Delgadez moderada ")
elif imc >= 18.50 and imc <= 24.99 :
    print("Normal")
elif imc >= 25.00 and imc <= 29.99:
    print("Sobrepeso, te estas pasando un poquito")
elif imc >= 30.00 and imc <= 34.99:
    print("Obsesidad leve, que te sucerdio")
elif imc >= 35.00 and imc <=39.99:
    print("Obesidad media, que te panzo")
elif imc >= 40.00 and imc > 40.00:
    print*("Obesidad morbida, hace cuantos kilos que no nos vemos")

