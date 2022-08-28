
contador = 1
while contador<=3:
    
    c = (input("ingrerse su contrasena con un numero entero por delante: "))
#no es necesario el for aqui 
    for i in c[0]:
        if c[0].isnumeric():
            print(f"{c[0]}, es numerico, contrasena validada")
        elif True:
            print("invalidado")
        contador +=1


    c2= input("Ingrese su nueva contrasena nuevamente:  ")
    if c2==c:
        print("Contrasenas coniciden")
    else:
        print("Contrasenas no coinciden")
        contador +=1
        if contador == 3:
            print("Has fallado en 3 intentos de contrasena")
        contador = contador +1
