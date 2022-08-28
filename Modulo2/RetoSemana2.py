yearA = int(input("ingrese el Año actual: "))
yearB = int(input("Un anio cualquiera: "))

difyears= yearA-yearB

if difyears > 0:
    if difyears ==1:
        print(f"ha pasado un año desde {yearB}")
    elif difyears == -1:
        print(f"falta un año para el {yearB}")
    elif difyears > 0:
        print(f"han pasado {difyears} años desde  el {yearB}")
elif difyears < 0:
    print(f'falta  {difyears*-1} año para el año {yearB}') 
elif yearA == yearB:
    print("Ingresaste el mismo año")



